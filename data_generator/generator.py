from itertools import count, islice
import random

from faker import Faker

from . import Account, Assignment, BusinessSector, Meeting, Mentee, MenteeMessage, MenteeSkill, Mentor, MentorMessage, MentorSkill, Skill, Workshop, printe
from .compute_bytea_hash import ComputeByteaHash

FAKE: Faker = None

ACCOUNT_SEQ = 0
MENTORS_SEQ = 0
MENTEES_SEQ = 0
MENTEE_MESSAGE_SEQ = 0
MENTOR_MESSAGE_SEQ = 0

MENTOR_SKILL_SEQ = 0
MENTEE_SKILL_SEQ = 0

PASSWORD_SALT: bytes = None

ASSIGNMENT_SEQ = 0
WORKSHOP_SEQ = 0
MEETING_SEQ = 0

POSSIBLE_MEETING_WORKSHOP_TIME = [15, 20, 30, 45, 60, 80, 90, 120, 150]
MAX_ASSIGNMENTS_PER_MENTOR = 5


def RandomPartition(input, n):
    division = len(input) / float(n)
    result = []

    for i in range(n):
        i1 = int(round(division * i))
        i2 = int(round(division * (i + 1)))
        result.append(input[i1:i2])

    return result


# Just to make sure the generated password hashes do not pollute the Git log
def Initialise(pure_random: bool):
    global FAKE
    global PASSWORD_SALT

    if not pure_random:
        random.seed(20220306)
        Faker.seed(20220306)
        PASSWORD_SALT = b'$2b$12$GA0FQtHmlwBHFA2NOM26Eu'

    FAKE = Faker()


def GenerateBusinessSectors() -> list[BusinessSector]:
    printe(f"Generating default business sectors...")

    sectors = [
        BusinessSector(1, "Private Bank"),
        BusinessSector(2, "Corporate Bank"),
        BusinessSector(3, "Asset Management"),
        BusinessSector(4, "Investment Bank"),
    ]

    return sectors


def GenerateAccounts(count: int, businessSectors: list[BusinessSector]) -> list[Account]:
    global ACCOUNT_SEQ
    printe(f"Generating {count} accounts...")

    accounts = []
    for i in range(count):
        ACCOUNT_SEQ += 1
        profile = FAKE.profile()
        account = Account(ACCOUNT_SEQ,
                          profile["name"],
                          FAKE.date_between(start_date='-40y', end_date='-18y'),
                          profile["mail"],  # Email
                          ComputeByteaHash(profile["mail"], PASSWORD_SALT),  # Password
                          random.choice(businessSectors))
        accounts.append(account)

        if i % 10 == 0:
            printe(f"    {i} out of {count} ...")

    return accounts


def GenerateMentors(accounts: list[Account]) -> list[Mentor]:
    global MENTORS_SEQ
    printe("Generate mentors...")

    mentors = []
    for a in accounts:
        MENTORS_SEQ += 1
        mentors.append(Mentor(MENTORS_SEQ, a))

    return mentors


def GenerateMentees(accounts: list[Account]) -> list[Mentee]:
    global MENTEES_SEQ
    printe("Generate mentees...")

    mentees = []
    for a in accounts:
        MENTEES_SEQ += 1
        mentees.append(Mentee(MENTEES_SEQ, a))

    return mentees


def GenerateMentorMessages(mentors: list[Mentor], count: int) -> list[MentorMessage]:
    global MENTOR_MESSAGE_SEQ
    printe(f"Generate {count} mentor messages...")

    messages = []
    for _ in range(count):
        MENTOR_MESSAGE_SEQ += 1
        chosenMentor = random.choice(mentors)
        messages.append(MentorMessage(MENTOR_MESSAGE_SEQ, chosenMentor, f"Message to mentor_{chosenMentor.id}: {FAKE.text()}"))
    return messages


def GenerateMenteeMessages(mentees: list[Mentee], count: int) -> list[MenteeMessage]:
    global MENTEE_MESSAGE_SEQ
    printe(f"Generate {count} mentee messages...")

    messages = []
    for _ in range(count):
        MENTEE_MESSAGE_SEQ += 1
        chosenMentee = random.choice(mentees)
        messages.append(MenteeMessage(MENTEE_MESSAGE_SEQ, chosenMentee, f"Message to mentee_{chosenMentee.id}: {FAKE.text()}"))
    return messages


def GenerateSkills(count: int) -> list[Skill]:
    printe(f"Generating {count} skills...")
    return [Skill(i, "Skill " + str(i)) for i in range(count)]


def AllocateMentorSkills(skills: list[Skill], mentors: list[Mentor], *, maxSkillsPerMentor: int, minSkillsPerMentor: int = 2) -> list[MentorSkill]:
    global MENTOR_SKILL_SEQ
    printe(f"Generating skills for {len(mentors)} mentors with skill range from {minSkillsPerMentor} to {maxSkillsPerMentor}")

    mentorSkills = []

    if len(skills) < maxSkillsPerMentor or len(skills) < minSkillsPerMentor or minSkillsPerMentor < 0:
        printe("ERROR: Max skill count is more than the number of given skills.")
        exit(1)

    for mentor in mentors:
        skillsCount = random.randrange(minSkillsPerMentor, maxSkillsPerMentor)
        randomSkills = random.sample(skills, skillsCount)
        for skill in randomSkills:
            MENTOR_SKILL_SEQ += 1
            mentorSkills.append(MentorSkill(MENTOR_SKILL_SEQ, mentor, skill))

    return mentorSkills


def AllocateMenteeSkills(skills: list[Skill], mentees: list[Mentee], *, maxSkillsPerMentee: int, minSkillsPerMentee: int = 1) -> list[MenteeSkill]:
    global MENTEE_SKILL_SEQ
    printe(f"Generating skills for {len(mentees)} mentees with skill range from {minSkillsPerMentee} to {maxSkillsPerMentee}")

    menteeSkills = []

    if len(skills) < maxSkillsPerMentee or len(skills) < minSkillsPerMentee or minSkillsPerMentee < 0:
        printe("ERROR: Max skill count is more than the number of given skills.")
        exit(1)

    for mentee in mentees:
        skillsCount = random.randrange(minSkillsPerMentee, maxSkillsPerMentee)
        randomSkills = random.sample(skills, skillsCount)
        for skill in randomSkills:
            MENTEE_SKILL_SEQ += 1
            menteeSkills.append(MenteeSkill(MENTEE_SKILL_SEQ, mentee, skill))

    return menteeSkills


def GenerateAssignment(mentors: list[Mentor], mentees: list[Mentee], *, hasFullyAssigned: bool, hasEmpty: bool) -> list[Assignment]:
    global ASSIGNMENT_SEQ
    printe(f"Generating assignments for {len(mentors)} mentors and {len(mentees)} mentees...")
    printe(f" -> With{'' if hasEmpty else 'out'} empty assginments")
    printe(f" -> With{'' if hasFullyAssigned else 'out'} full assignments")

    assignments = []

    availableMentors = mentors.copy()
    availableMentees = mentees.copy()

    random.shuffle(availableMentors)
    random.shuffle(availableMentees)

    if hasEmpty:
        emptyMentorsCount = random.randint(1, max(1, int(len(availableMentors) / 5)))
        printe(f"    Preserving {emptyMentorsCount} unassigned mentors...")
        availableMentors = availableMentors[emptyMentorsCount:]

    if hasFullyAssigned:
        fullyAssignedMentorsCount = random.randint(1, max(1, int(len(availableMentors) / 6)))
        printe(f"    Preserving {fullyAssignedMentorsCount} fully-assigned mentors...")

        fullyAssignedMentors = availableMentors[:fullyAssignedMentorsCount]
        availableMentors = availableMentors[fullyAssignedMentorsCount:]

        for mentor in fullyAssignedMentors:
            for _ in range(MAX_ASSIGNMENTS_PER_MENTOR):
                ASSIGNMENT_SEQ += 1
                mentee = random.choice(availableMentees)
                assignments.append(Assignment(ASSIGNMENT_SEQ, mentor, mentee))
                availableMentees.remove(mentee)

    # availableMentors = availableMentors * MAX_ASSIGNMENTS_PER_MENTOR

    mentorApCount = dict([(m, 0) for m in availableMentors])

    for mentee in availableMentees:
        ASSIGNMENT_SEQ += 1

        # Choose mentor for this mentee
        candidateMentors = [m for (m, c) in mentorApCount.items() if c < MAX_ASSIGNMENTS_PER_MENTOR - (0 if hasFullyAssigned else 1)]

        if len(candidateMentors) == 0:
            printe(f"ERROR: Insufficient mentors.")
            exit(1)

        mentor = random.choice(candidateMentors)
        mentorApCount[mentor] += 1
        assignments.append(Assignment(ASSIGNMENT_SEQ, mentor, mentee))

    return assignments


def GenerateWorkshop(skills: list[Skill], count: int, *, past: bool = True, future: bool = True) -> list[Workshop]:
    global WORKSHOP_SEQ
    printe(f"Generating {count} workshops for {len(skills)} skills...")
    printe(f" -> With{'' if past else 'out'} past events")
    printe(f" -> With{'' if future else 'out'} future events")

    if (not past) and (not future):
        printe("???")
        exit(1)

    pastCount = 0
    futureCount = 0

    selectedSkills = random.choices(skills, k=count)
    workshops = []

    for skill in selectedSkills:
        WORKSHOP_SEQ += 1

        isFuture = random.choice([True, False])

        if isFuture:
            futureCount += 1
            workshopTime = FAKE.future_datetime(end_date='+30d', tzinfo=None)
        else:
            pastCount += 1
            workshopTime = FAKE.past_datetime(start_date='-30d', tzinfo=None)

        workshops.append(Workshop(WORKSHOP_SEQ, skill, workshopTime, random.choice(POSSIBLE_MEETING_WORKSHOP_TIME), "https://example.com/Workshop_" + str(WORKSHOP_SEQ)))

    printe(f" -> Generated {pastCount} past and {futureCount} future workshops.")
    return workshops


def GenerateMeetings(assignments: list[Assignment], count: int, *, past: bool = True, future: bool = True) -> list[Assignment]:
    global MEETING_SEQ
    printe(f"Generating {count} meetings for {len(assignments)} assignments...")
    printe(f" -> With{'' if past else 'out'} past events")
    printe(f" -> With{'' if future else 'out'} future events")

    if (not past) and (not future):
        printe("???")
        exit(1)

    pastCount = 0
    futureCount = 0

    selectedAssignments = random.choices(assignments, k=count)
    meetings = []

    for assignment in selectedAssignments:
        MEETING_SEQ += 1

        isFuture = random.choice([True, False])

        if isFuture:
            futureCount += 1
            meethingTime = FAKE.future_datetime(end_date='+30d', tzinfo=None)
        else:
            pastCount += 1
            meethingTime = FAKE.past_datetime(start_date='-30d', tzinfo=None)

        meetings.append(Meeting(MEETING_SEQ, assignment, meethingTime, random.choice(POSSIBLE_MEETING_WORKSHOP_TIME), "https://example.com/Meeting_" + str(MEETING_SEQ)))

    printe(f" -> Generated {pastCount} past and {futureCount} future meetings.")
    return meetings

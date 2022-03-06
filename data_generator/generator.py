import random
from . import Account, Assignment, BusinessSector, Mentee, MenteeMessage, MenteeSkill, Mentor, MentorMessage, MentorSkill, Skill, Workshop, printe
from .compute_bytea_hash import ComputeByteaHash
from faker import Faker

FAKE: Faker = None

ACCOUNT_SEQ = 0
MENTORS_SEQ = 0
MENTEES_SEQ = 0
MENTEE_MESSAGE_SEQ = 0
MENTOR_MESSAGE_SEQ = 0

MENTOR_SKILL_SEQ = 0
MENTEE_SKILL_SEQ = 0

PASSWORD_SALT: bytes = None


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
            printe(f"  {i} out of {count} ...")

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


def AllocateMentorSkills(skills: list[Skill], mentors: list[Mentor], maxSkillsPerMentor: int, minSkillsPerMentor: int = 2) -> list[MentorSkill]:
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


def AllocateMenteeSkills(skills: list[Skill], mentees: list[Mentee], maxSkillsPerMentee: int, minSkillsPerMentee: int = 1) -> list[MenteeSkill]:
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


def GenerateAssignment(mentors: list[Mentor], mentees: list[Mentee], hasFullyAssigned: bool, hasEmpty: bool) -> list[Assignment]:
    pass


def GenerateWorkshop(skills: list[Skill], count: int, past: bool = True, future: bool = True) -> list[Workshop]:
    pass


def GenerateMeeing(assignments: list[Assignment], count: int, past: bool = True, future: bool = True) -> list[Assignment]:
    pass

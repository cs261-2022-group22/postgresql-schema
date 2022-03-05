import random
from . import Account, BusinessSector, Mentee, MenteeMessage, Mentor, MentorMessage, printe
from .compute_bytea_hash import ComputeByteaHash
from faker import Faker

FAKE = Faker()

ACCOUNT_SEQ = 0
MENTORS_SEQ = 0
MENTEES_SEQ = 0
MENTEE_MESSAGE_SEQ = 0
MENTOR_MESSAGE_SEQ = 0


def GenerateBusinessSectors():
    printe(f"Generating default business sectors...")

    sectors = [
        BusinessSector(1, "Private Bank"),
        BusinessSector(2, "Corporate Bank"),
        BusinessSector(3, "Asset Management"),
        BusinessSector(4, "Investment Bank"),
    ]

    return sectors


def GenerateAccounts(count: int, businessSectors: list[BusinessSector]):
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
                          ComputeByteaHash(profile["mail"]),  # Password
                          random.choice(businessSectors))
        accounts.append(account)

        if i % 10 == 0:
            printe(f"  {i} out of {count} ...")

    return accounts


def GenerateMentors(accounts: list[Account]):
    global MENTORS_SEQ
    printe("Generate mentors...")

    mentors = []
    for a in accounts:
        MENTORS_SEQ += 1
        mentors.append(Mentor(MENTORS_SEQ, a))

    return mentors


def GenerateMentees(accounts: list[Account]):
    global MENTEES_SEQ
    printe("Generate mentees...")

    mentees = []
    for a in accounts:
        MENTEES_SEQ += 1
        mentees.append(Mentee(MENTEES_SEQ, a))

    return mentees


def GenerateMentorMessages(mentors: list[Mentor], count: int):
    global MENTOR_MESSAGE_SEQ
    printe(f"Generate {count} mentor messages...")

    messages = []
    for _ in range(count):
        MENTOR_MESSAGE_SEQ += 1
        chosenMentor = random.choice(mentors)
        messages.append(MentorMessage(MENTOR_MESSAGE_SEQ, chosenMentor, f"Message to mentor_{chosenMentor.id}: {FAKE.text()}"))
    return messages


def GenerateMenteeMessages(mentees: list[Mentee], count: int):
    global MENTEE_MESSAGE_SEQ
    printe(f"Generate {count} mentee messages...")

    messages = []
    for _ in range(count):
        MENTEE_MESSAGE_SEQ += 1
        chosenMentee = random.choice(mentees)
        messages.append(MenteeMessage(MENTEE_MESSAGE_SEQ, chosenMentee, f"Message to mentee_{chosenMentee.id}: {FAKE.text()}"))
    return messages

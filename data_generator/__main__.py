import random
from . import generator


def GenerateSQLSection(name, list, gen_comment=None):
    print("--", name)
    for e in list:
        print(e, "" if gen_comment is None else "-- " + gen_comment(e))
    print()


if __name__ == "__main__":
    NUMBER_OF_MENTORS = 20
    NUMBER_OF_MENTEES = 60

    BusinessSectors = generator.GenerateBusinessSectors()
    GenerateSQLSection("Business Sectors", BusinessSectors)

    Accounts = generator.GenerateAccounts(NUMBER_OF_MENTORS + NUMBER_OF_MENTEES, BusinessSectors)
    GenerateSQLSection("Accounts", Accounts)

    random_accounts = Accounts.copy()
    random.shuffle(random_accounts)

    # =========== MENTORS ===========
    mentor_accounts = random_accounts[:NUMBER_OF_MENTORS]
    Mentors = generator.GenerateMentors(mentor_accounts)
    GenerateSQLSection("Mentors", Mentors, lambda m: f"Account: {m.account.email}")

    MentorMessagesCount = random.randrange(NUMBER_OF_MENTORS, 4 * NUMBER_OF_MENTORS)
    MentorMessages = generator.GenerateMentorMessages(Mentors, MentorMessagesCount)
    GenerateSQLSection("Mentor Messages", MentorMessages)

    # =========== MENTEES ===========
    mentee_accounts = random_accounts[NUMBER_OF_MENTORS:]
    Mentees = generator.GenerateMentees(mentee_accounts)
    GenerateSQLSection("Mentees", Mentees, lambda m: f"Account: {m.account.email}")

    MenteeMessageCount = random.randrange(NUMBER_OF_MENTEES, 3 * NUMBER_OF_MENTEES)
    MenteeMessages = generator.GenerateMenteeMessages(Mentees, MenteeMessageCount)
    GenerateSQLSection("Mentee Messages", MenteeMessages)

    pass

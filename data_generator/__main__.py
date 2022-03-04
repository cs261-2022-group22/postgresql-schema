import math
import random
from . import generator


def PrintList(name, list):
    print("--", name)
    for e in list:
        print(e)
    print()


if __name__ == "__main__":
    NUMBER_OF_MENTORS = 20
    NUMBER_OF_MENTEES = 60

    BusinessSectors = generator.GenerateBusinessSectors()
    PrintList("Business Sectors", BusinessSectors)

    Accounts = generator.GenerateAccounts(NUMBER_OF_MENTORS + NUMBER_OF_MENTEES, BusinessSectors)
    PrintList("Accounts", Accounts)

    random_accounts = Accounts.copy()
    random.shuffle(random_accounts)

    # =========== MENTORS ===========
    mentor_accounts = random_accounts[:NUMBER_OF_MENTORS]
    Mentors = generator.GenerateMentors(mentor_accounts)
    PrintList("Mentors", Mentors)

    MentorMessagesCount = random.randrange(NUMBER_OF_MENTORS, 5 * NUMBER_OF_MENTORS)
    MentorMessages = generator.GenerateMentorMessages(Mentors, MentorMessagesCount)
    PrintList("Mentor Messages", MentorMessages)

    # =========== MENTEES ===========
    mentee_accounts = random_accounts[NUMBER_OF_MENTORS:]
    Mentees = generator.GenerateMentees(mentee_accounts)
    PrintList("Mentees", Mentees)

    MenteeMessageCount = random.randrange(NUMBER_OF_MENTEES, 4 * NUMBER_OF_MENTEES)
    MenteeMessages = generator.GenerateMenteeMessages(Mentees, MenteeMessageCount)
    PrintList("Mentee Messages", MenteeMessages)

    pass

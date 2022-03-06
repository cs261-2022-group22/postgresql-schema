import random

from faker import Faker

from . import Account, Mentee, MenteeMessage, MenteeSkill, Mentor, MentorMessage, MentorSkill, generator as G


def GenerateSQLSection(name, list, gen_comment=None):
    print("--", name)
    for e in list:
        if gen_comment is not None:
            print(e, f"-- {gen_comment(e)}")
        else:
            print(e)
    print("\n")


def comment_gen_account_bs(a: Account):
    return f"'{a.bs.name}'"


def comment_gen_mentor_account(m: Mentor):
    return f"Mentor ({m.account.name} <{m.account.email}>, {comment_gen_account_bs(m.account)})"


def comment_gen_mentee_account(m: Mentee):
    return f"Mentee ({m.account.name} <{m.account.email}>, {comment_gen_account_bs(m.account)})"


def comment_gen_mentor_skills(m: MentorSkill):
    return f"Skill '{m.skill.name}' for {comment_gen_mentor_account(m.mentor)}"


def comment_gen_mentee_skills(m: MenteeSkill):
    return f"Skill '{m.skill.name}' for {comment_gen_mentee_account(m.mentee)}"


def comment_gen_mentor_message(m: MentorMessage):
    return f"Message to {comment_gen_mentor_account(m.mentor)}"


def comment_gen_mentee_message(m: MenteeMessage):
    return f"Message to {comment_gen_mentee_account(m.mentee)}"


PURE_RANDOM = False

if __name__ == "__main__":
    G.Initialise(PURE_RANDOM)

    NUMBER_OF_MENTORS = 20
    NUMBER_OF_MENTEES = 60
    NUMBER_OF_SKILLS = 15

    BusinessSectors = G.GenerateBusinessSectors()

    Accounts = G.GenerateAccounts(NUMBER_OF_MENTORS + NUMBER_OF_MENTEES, BusinessSectors)

    random_accounts = Accounts.copy()
    random.shuffle(random_accounts)

    # =========== MENTORS ===========
    mentor_accounts = random_accounts[:NUMBER_OF_MENTORS]
    Mentors = G.GenerateMentors(mentor_accounts)

    MentorMessagesCount = random.randrange(NUMBER_OF_MENTORS, 4 * NUMBER_OF_MENTORS)
    MentorMessages = G.GenerateMentorMessages(Mentors, MentorMessagesCount)

    # =========== MENTEES ===========
    mentee_accounts = random_accounts[NUMBER_OF_MENTORS:]
    Mentees = G.GenerateMentees(mentee_accounts)

    MenteeMessageCount = random.randrange(NUMBER_OF_MENTEES, 3 * NUMBER_OF_MENTEES)
    MenteeMessages = G.GenerateMenteeMessages(Mentees, MenteeMessageCount)

    # =========== SKILLS ===========
    Skills = G.GenerateSkills(NUMBER_OF_SKILLS)
    MentorSkills = G.AllocateMentorSkills(Skills, Mentors, 8)
    MenteeSkills = G.AllocateMenteeSkills(Skills, Mentees, 4, 2)

    GenerateSQLSection("Business Sectors", BusinessSectors)
    GenerateSQLSection("Accounts", Accounts, comment_gen_account_bs)
    GenerateSQLSection("Mentors", Mentors, comment_gen_mentor_account)
    GenerateSQLSection("Mentor Messages", MentorMessages, comment_gen_mentor_message)
    GenerateSQLSection("Mentees", Mentees, comment_gen_mentee_account)
    GenerateSQLSection("Mentee Messages", MenteeMessages, comment_gen_mentee_message)
    GenerateSQLSection("Skills", Skills)
    GenerateSQLSection("Mentor Skills", MentorSkills, comment_gen_mentor_skills)
    GenerateSQLSection("Mentee Skills", MenteeSkills, comment_gen_mentee_skills)

    pass

import random
from freezegun import freeze_time

from . import Account, Assignment, Meeting, Mentee, MenteeMessage, MenteeSkill, Mentor, MentorMessage, MentorSkill, Workshop, generator as G


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


def comment_gen_mentor_skill(m: MentorSkill):
    return f"Skill '{m.skill.name}' for {comment_gen_mentor_account(m.mentor)}"


def comment_gen_mentee_skill(m: MenteeSkill):
    return f"Skill '{m.skill.name}' for {comment_gen_mentee_account(m.mentee)}"


def comment_gen_mentor_message(m: MentorMessage):
    return f"Message to {comment_gen_mentor_account(m.mentor)}"


def comment_gen_mentee_message(m: MenteeMessage):
    return f"Message to {comment_gen_mentee_account(m.mentee)}"


def comment_gen_assignment(a: Assignment):
    return f"{comment_gen_mentor_account(a.mentor)} <=> {comment_gen_mentee_account(a.mentee)}"


def comment_gen_workshop(w: Workshop):
    return f"For skill '{w.skill.name}'"


def comment_gen_meeting(w: Meeting):
    return comment_gen_assignment(w.assignment)


PURE_RANDOM = False


def main():
    G.Initialise(PURE_RANDOM)

    NUMBER_OF_MENTORS = 20
    NUMBER_OF_MENTEES = 60
    NUMBER_OF_WORKSHOPS = 40
    NUMBER_OF_MEETINGS = 40

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
    Skills = G.GenerateSkills()
    MentorSkills = G.AllocateMentorSkills(Skills, Mentors, maxSkillsPerMentor=5)
    MenteeSkills = G.AllocateMenteeSkills(Skills, Mentees, maxSkillsPerMentee=4, minSkillsPerMentee=1)

    # =========== Assignments ===========
    Assignments = G.GenerateAssignment(Mentors, Mentees, hasEmpty=False, hasFullyAssigned=True)

    # =========== Workshops ===========
    Workshops = G.GenerateWorkshop(Skills, NUMBER_OF_WORKSHOPS, past=True, future=True)

    # =========== Meetings ===========
    Meetings = G.GenerateMeetings(Assignments, NUMBER_OF_MEETINGS, past=True, future=True)

    # =========== Milestones ===========
    Milestones = G.GenerateMilestones(Mentees)

    Mentees[0].account.passwordHash = R"E'\\x243262243132245159367569413552717a613166754f4b533478524c4f5041724a33645270774970376f334e703671324f44524c4859424256755632'"
    Mentees[0].account.email = "test-mentee@gmail.com"
    Mentees[0].account.name = "Test Mentee Account"

    Mentors[0].account.passwordHash = R"E'\\x243262243132245159367569413552717a613166754f4b533478524c4f5041724a33645270774970376f334e703671324f44524c4859424256755632'"
    Mentors[0].account.email = "test@gmail.com"
    Mentors[0].account.name = "Test Mentor Account"

    GenerateSQLSection("Business Sectors", BusinessSectors)
    GenerateSQLSection("Accounts", Accounts, comment_gen_account_bs)
    GenerateSQLSection("Mentors", Mentors, comment_gen_mentor_account)
    GenerateSQLSection("Mentor Messages", MentorMessages, comment_gen_mentor_message)
    GenerateSQLSection("Mentees", Mentees, comment_gen_mentee_account)
    GenerateSQLSection("Mentee Messages", MenteeMessages, comment_gen_mentee_message)
    GenerateSQLSection("Skills", Skills)
    GenerateSQLSection("Mentor Skills", MentorSkills, comment_gen_mentor_skill)
    GenerateSQLSection("Mentee Skills", MenteeSkills, comment_gen_mentee_skill)
    GenerateSQLSection("Assignments", Assignments, comment_gen_assignment)
    GenerateSQLSection("Workshops", Workshops, comment_gen_workshop)
    GenerateSQLSection("Meetings", Meetings, comment_gen_meeting)
    GenerateSQLSection("Milestones", Milestones)

    pass


if __name__ == "__main__":
    with freeze_time("2022-03-06"):
        main()

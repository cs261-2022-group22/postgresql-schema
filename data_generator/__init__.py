from datetime import date, datetime
import sys


def printe(*args, **kwargs):
    """Print Messages to `stderr` instead of `stdout`
    """
    print(*args, file=sys.stderr, **kwargs)


class BusinessSector:
    def __init__(self, _id, _name) -> None:
        self.id = _id
        self.name = _name
        pass

    def __str__(self) -> str:
        return f"INSERT INTO BusinessSector VALUES({self.id}, '{self.name}');"


class Account:
    def __init__(self, _id: int, _name: str, _dob: date, _email: str, _passwordHash: str, _businessSector: BusinessSector) -> None:
        self.id = _id
        self.name = _name
        self.dob = _dob
        self.email = _email
        self.passwordHash = _passwordHash
        self.bs = _businessSector
        pass

    def __str__(self) -> str:
        return f"INSERT INTO Account VALUES({self.id}, '{self.name}', '{self.email}', {self.passwordHash}, DATE '{self.dob}', {self.bs.id});"


class Mentor:
    def __init__(self, _id: int, _account: Account) -> None:
        self.id = _id
        self.account = _account
        pass

    def __str__(self) -> str:
        return f"INSERT INTO Mentor VALUES({self.id}, {self.account.id});"


class Mentee:
    def __init__(self, _id: int, _account: Account) -> None:
        self.id = _id
        self.account = _account
        pass

    def __str__(self) -> str:
        return f"INSERT INTO Mentee VALUES({self.id}, {self.account.id});"


class MentorMessage:
    def __init__(self, _id: int, _mentor: Mentor,  _message: str) -> None:
        self.id = _id
        self.mentor = _mentor
        self.message = _message
        pass

    def __str__(self) -> str:
        return f"INSERT INTO MentorMessage VALUES({self.id}, {self.mentor.id}, '{self.message}');"


class MenteeMessage:
    def __init__(self, _id: int, _mentee: Mentee,  _message: str) -> None:
        self.id = _id
        self.mentee = _mentee
        self.message = _message
        pass

    def __str__(self) -> str:
        return f"INSERT INTO MenteeMessage VALUES({self.id}, {self.mentee.id}, '{self.message}');"


class Skill:
    def __init__(self, _id: int, _name: str) -> None:
        self.id = _id
        self.name = _name
        pass

    def __str__(self) -> str:
        return f"INSERT INTO Skill VALUES({self.id}, '{self.name}');"


class Workshop:
    def __init__(self, _id: int, _skill: Skill, _start: datetime, _duration_minutes: int, _link: str) -> None:
        self.id = _id
        self.skill = _skill
        self.start = _start
        self.duration_minutes = _duration_minutes
        self.link = _link
        pass

    def __str__(self) -> str:
        return f"INSERT INTO Workshop VALUES({self.id}, {self.skill.id}, '{self.link}', '{self.start}', {self.duration_minutes});"


class Assignment:
    def __init__(self, _id: int, _mentor: Mentor, _mentee: Mentee) -> None:
        self.id = _id
        self.mentor = _mentor
        self.mentee = _mentee
        pass

    def __str__(self) -> str:
        return f"INSERT INTO Assignment VALUES({self.id}, {self.mentor.id}, {self.mentee.id});"


class Meeting:
    def __init__(self, _id: int, _assignment: Assignment, _start: datetime, _duration_minutes: int, _link: str) -> None:
        self.id = _id
        self.assignment = _assignment
        self.start = _start
        self.duration_minutes = _duration_minutes
        self.link = _link
        pass

    def __str__(self) -> str:
        return f"INSERT INTO Meeting VALUES({self.id}, {self.assignment.id}, '{self.link}', '{self.start}', {self.duration_minutes});"


class MentorSkill:
    def __init__(self, _id: int, _mentor: Mentor, _skill: Skill) -> None:
        self.id = _id
        self.mentor = _mentor
        self.skill = _skill

    def __str__(self) -> str:
        return f"INSERT INTO MentorSkill VALUES({self.id}, {self.mentor.id}, {self.skill.id});"


class MenteeSkill:
    def __init__(self, _id: int, _mentee: Mentee, _skill: Skill) -> None:
        self.id = _id
        self.mentee = _mentee
        self.skill = _skill

    def __str__(self) -> str:
        return f"INSERT INTO MenteeSkill VALUES({self.id}, {self.mentee.id}, {self.skill.id});"

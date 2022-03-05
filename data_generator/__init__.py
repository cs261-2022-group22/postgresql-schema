from datetime import date
import sys
import bcrypt


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
        self.mentee = _mentor
        self.message = _message
        pass

    def __str__(self) -> str:
        return f"INSERT INTO MentorMessage VALUES({self.id}, {self.mentee.id}, '{self.message}');"


class MenteeMessage:
    def __init__(self, _id: int, _mentee: Mentee,  _message: str) -> None:
        self.id = _id
        self.mentee = _mentee
        self.message = _message
        pass

    def __str__(self) -> str:
        return f"INSERT INTO MenteeMessage VALUES({self.id}, {self.mentee.id}, '{self.message}');"

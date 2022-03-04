from datetime import date
import sys
import bcrypt


def printe(*args, **kwargs):
    """Print Messages to `stderr` instead of `stdout`
    """
    print(*args, file=sys.stderr, **kwargs)


def GenerateHash(password: str):
    passwordPlainBytes = password.encode("utf-8")
    passwordHashBytes = bcrypt.hashpw(passwordPlainBytes, bcrypt.gensalt())
    return "E'" + "\\\\x" + (passwordHashBytes.hex()) + "'"


class BusinessSector:
    def __init__(self, _id, _name) -> None:
        self.id = _id
        self.name = _name
        pass

    def __str__(self) -> str:
        return f"INSERT INTO BusinessSector VALUES({self.id}, '{self.name}');"


class Account:
    def __init__(self, _id: int, _name: str, _dob: date, _email: str, _password: str, _businessSector: BusinessSector) -> None:
        self.id = _id
        self.name = _name
        self.dob = _dob
        self.email = _email
        self.password = GenerateHash(_password)
        self.bsId = _businessSector.id
        pass

    def __str__(self) -> str:
        return f"INSERT INTO Account VALUES({self.id}, '{self.name}', '{self.email}', {self.password}, DATE '{self.dob}', {self.bsId});"


class Mentor:
    def __init__(self, _id: int, _account: Account) -> None:
        self.id = _id
        self.accountId = _account.id
        pass

    def __str__(self) -> str:
        return f"INSERT INTO Mentor VALUES({self.id}, {self.accountId});"


class Mentee:
    def __init__(self, _id: int, _account: Account) -> None:
        self.id = _id
        self.accountId = _account.id
        pass

    def __str__(self) -> str:
        return f"INSERT INTO Mentee VALUES({self.id}, {self.accountId});"


class MentorMessage:
    def __init__(self, _id: int, _mentor: Mentor,  _message: str) -> None:
        self.id = _id
        self.menteeId = _mentor.id
        self.message = _message
        pass

    def __str__(self) -> str:
        return f"INSERT INTO MentorMessage VALUES({self.id}, {self.menteeId}, '{self.message}');"


class MenteeMessage:
    def __init__(self, _id: int, _mentee: Mentee,  _message: str) -> None:
        self.id = _id
        self.menteeId = _mentee.id
        self.message = _message
        pass

    def __str__(self) -> str:
        return f"INSERT INTO MenteeMessage VALUES({self.id}, {self.menteeId}, '{self.message}');"

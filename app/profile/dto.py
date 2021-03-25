from dataclasses import dataclass


@dataclass
class UserDTO:
    username: str
    email: str
    password: str

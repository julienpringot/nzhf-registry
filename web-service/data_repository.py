
from dataclasses import dataclass
from enum import Enum

class UserRole(Enum):
    NZHF_ADMIN = 'NZHF Admin'
    CLUB_ADMIN = 'Club Admin'

@dataclass
class User:
    email: str
    full_name: str
    role: UserRole

class UserRepository:
    def __init__(self) -> None:
        self._users_by_email = {}

    def add(self, user: User):
        self._users_by_email[user.email] = user

    def get(self, email):
        return self._users_by_email[email]
    
    def get_all(self):
        return self._users_by_email.values()

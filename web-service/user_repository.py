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
        self.add(User(email='jupringot@gmail.com', full_name='Julien Pringot', role=UserRole.NZHF_ADMIN))
        self.add(User(email='paul.pringot@gmail.com', full_name='Paul Pringot', role=UserRole.NZHF_ADMIN))

    def add(self, user: User):
        self._users_by_email[user.email] = user

    def get(self, email):
        return self._users_by_email[email]
    
    def get_all(self):
        return self._users_by_email.values()
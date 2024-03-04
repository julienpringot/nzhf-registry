# Create instances of the User dataclass
from data_repository import User, UserRepository, UserRole

MockUserRepo = UserRepository()
MockUserRepo.add(User(email='jupringot@gmail.com', full_name='Julien Pringot', role=UserRole.NZHF_ADMIN))
MockUserRepo.add(User(email='paul.pringot@gmail.com', full_name='Paul Pringot', role=UserRole.NZHF_ADMIN))

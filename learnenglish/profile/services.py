from .models import User
from .dto import UserDTO


def create_user(user_data: UserDTO) -> User:
    return User.objects.create_user(user_data)


def create_superuser(user_data: UserDTO) -> User:
    return User.objects.create_superuser(user_data)

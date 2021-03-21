from django.contrib.auth.models import BaseUserManager
from typing import TYPE_CHECKING

from .dto import UserDTO

if TYPE_CHECKING:
    from .models import User


class UserManager(BaseUserManager):
    def create_user(self, user_data: UserDTO) -> 'User':
        user = self.model(
            username=user_data['username'], email=self.normalize_email(user_data['email']))

        user.set_password(user_data['password'])
        user.save()

        return user

    def create_superuser(self, user_data: UserDTO) -> 'User':
        user = self.create_user(user_data)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

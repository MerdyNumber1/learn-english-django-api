from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=56, verbose_name='имя')
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True, verbose_name='активен')
    is_staff = models.BooleanField(default=False, verbose_name='администратор')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    @property
    def registration_date(self) -> str:
        return self.created_at.strftime('%d.%m.%Y')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self) -> str:
        return str(self.email)

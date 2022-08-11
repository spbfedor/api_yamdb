from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class ROLES(Enum):
    user = 'Пользователь'
    moderator = 'Модератор'
    admin = 'Администратор'

    @classmethod
    def get_roles(cls):
        return [(role.name, role.value) for role in cls]

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Имя пользователя'
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Электронная почта'
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
        null=True
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        null=True
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='О себе',
    )
    role = models.CharField(
        max_length=20,
        choices=ROLES.get_roles(),
        default='user',
        verbose_name='Роль'
    )
    confirmation_code = models.CharField(
        max_length=50,
        default=''
    )
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

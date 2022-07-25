from django.contrib.auth.models import AbstractUser
from django.core.validators import (MinValueValidator, MaxValueValidator,
                                    RegexValidator)
from django.db import models

from api_yamdb.settings import CODE_LENGTH, EMAIL_LENGTH, USERNAME_LENGTH


# Проверка имени пользователя
class Validator(RegexValidator):
    regex = r'^[\w.@+-]+$'
    flags = 0


# Кастомный класс
class User(AbstractUser):

    # Роли
    ADMIN_ROLE = 'admin'
    MODERATOR_ROLE = 'moderator'
    USER_ROLE = 'user'

    # Права роли
    ACCESS_ROLES = (
        (USER_ROLE, 'user'),
        (MODERATOR_ROLE, 'moderator'),
        (ADMIN_ROLE, 'admin')
    )

    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=USERNAME_LENGTH,
        unique=True,
        validators=[Validator()],
    )

    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=EMAIL_LENGTH,
        blank=False,
        unique=True
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True
    )
    role = models.CharField(
        max_length=max(
            len(iteration[0]) for iteration in ACCESS_ROLES),
        choices=ACCESS_ROLES,
        default=USER_ROLE,
        blank=False,
        verbose_name='Роль'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Биография',
        help_text='Расскажите о себе'
    )
    confirmation_code = models.CharField(
        max_length=CODE_LENGTH,
        blank=True,
        null=True
    )

    # Проверка прав на соответствие роли
    @property
    def is_user(self):
        return self.role == self.USER_ROLE

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR_ROLE

    @property
    def is_admin(self):
        return (self.role == self.ADMIN_ROLE
                or self.is_superuser)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_user_code'
            ),
        ]


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateField()
    description = models.CharField(max_length=200)
    genres = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        related_name='titles'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='titles'
    )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'

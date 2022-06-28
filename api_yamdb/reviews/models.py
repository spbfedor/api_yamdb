from django.db import models
from django.contrib.auth.models import AbstractUser

#TODO Импортировать классы проверки полей

# Импорт настроек длины полей и кода из settings
from api_yamdb.settings import CODE_LENGTH, EMAIL_LENGTH, USERNAME_LENGTH

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
        unique=True
        #TODO Сделать валидацию имени пользователя
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
        #TODO Сделать валидацию кода подтверждения
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
                or self.is_staff)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_user_code'
            ),
        ]


class CategoryGenre(models.Model):

    pass


class Category(CategoryGenre):

    pass


class Genre(CategoryGenre):

    pass


class Title(models.Model):

    pass


class CommentReview(models.Model):

    pass


class Review(CommentReview):

    pass


class Comment(CommentReview):

    pass
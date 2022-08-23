from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import validate_not_future_year
from users.models import User


class Category(models.Model):
    name = models.CharField(
        'имя категории',
        max_length=256,
        db_index=True
    )
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name[:15]


class Genre(models.Model):
    name = models.CharField(
        'имя жанра',
        max_length=256,
        db_index=True
    )
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name[:15]


class Title(models.Model):
    name = models.CharField(
        'название',
        max_length=256,
        db_index=True
    )
    year = models.PositiveSmallIntegerField(
        'год выпуска',
        validators=[validate_not_future_year],
    )
    description = models.TextField('описание', blank=True, default='')
    genre = models.ManyToManyField(Genre)
    category = models.ForeignKey(
        Category,
        related_name='titles',
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'year', 'category'),
                name='unique_title',
            )
        ]

    def __str__(self):
        return self.name[:15]


class Review(models.Model):
    text = models.TextField('текст отзыва')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.PositiveSmallIntegerField(
        'оценка',
        validators=[
            MinValueValidator(1, 'минимальная оценка'),
            MaxValueValidator(10, 'максимальная оценка')
        ]
    )
    pub_date = models.DateTimeField('дата', auto_now_add=True)
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='reviews'
    )

    class Meta:
        ordering = ['pub_date']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review'
            )
        ]

    def __str__(self):
        return f'{self.title} {self.text[:15]}'


class Comment(models.Model):
    text = models.TextField('комментарий')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField('дата', auto_now_add=True)
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        ordering = ['pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.review} {self.text[:15]}'

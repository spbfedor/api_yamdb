from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()


class Comment(models.Model):
    pass


class Review(models.Model):
    pass


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateField()
    description = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
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
        null=True
    )

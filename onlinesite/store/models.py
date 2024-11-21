from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class Profile(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.PositiveSmallIntegerField(null=True, blank=True)
    STATUS_CHOICES = (
        ('pro', 'pro'),
        ('simple', 'Simple'),
    )
    status = models.CharField(max_length=18, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return self.username



class Country(models.Model):
    country_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=32)
    country = models.ForeignKey(Country, related_name="director", on_delete=models.CASCADE)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField()
    director_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=16)
    bio = models.TextField()
    age = models.PositiveIntegerField()
    actor_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.actor_name


class Janre(models.Model):
    janre_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.janre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    country = models.ForeignKey(Country, related_name="movie", on_delete=models.CASCADE)
    director = models.ForeignKey(Director, related_name="movie", on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, related_name="movie", on_delete=models.CASCADE)
    janre = models.ForeignKey(Janre, related_name="movie", on_delete=models.CASCADE)
    types = (
        (144, 144),
        (360, 360),
        (480, 480),
        (720, 720),
        (1080, 1080),
    )

    types = models.IntegerField(choices=types, default=720)
    movie_time = models.DateField(auto_now=True)
    description = models.TextField()
    movie_trailer = models.FileField(upload_to='vid/', verbose_name="Видео", null=True, blank=True)
    movie_image = models.ImageField(upload_to='image/')
    status_movie = (
        ('pro', 'Pro'),
        ('simple', 'simple'),

    )

    status_movie = models.CharField(max_length=18, choices=status_movie, default='class')

    def str(self):
        return f'{self.movie_name} - {self.country} - {self.director} - {self.actor} - {self.janre}'


class MovieLanguages(models.Model):
    language = models.CharField(max_length=32)
    video = models.ImageField(upload_to=True)
    movie = models.ForeignKey(Movie, related_name="MovieLanguages", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.language} - {self.movie}'


class Moments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_moments = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.movie


class Rating(models.Model):
    user = models.CharField(max_length=16)
    movie = models.ForeignKey(Movie, related_name="ratings", on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Рейтинг")
    parent = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.movie}'


class Favorite(models.Model):
    user = models.ForeignKey(Rating, related_name="favorite", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.created_date}'


class FavoriteMovie(models.Model):
    cart = models.CharField(max_length=16)
    movie = models.ForeignKey(Moments, related_name="favoritemovie", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cart} - {self.movie}'


class History(models.Model):
    user = models.ForeignKey(Rating, related_name="history", on_delete=models.CASCADE)
    movie = models.ForeignKey(Moments, related_name="history", on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} -{self.movie} - {self.viewed_at}'
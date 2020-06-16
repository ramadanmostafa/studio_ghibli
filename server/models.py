from django.db import models


GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
)


class People(models.Model):
    external_id = models.CharField(unique=True, max_length=512)
    name = models.CharField(max_length=512)
    gender = models.CharField(max_length=64, choices=GENDER_CHOICES, default='')
    age = models.CharField(max_length=512)
    eye_color = models.CharField(max_length=512)
    hair_color = models.CharField(max_length=512)


class Movie(models.Model):
    external_id = models.CharField(unique=True, max_length=512)
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=2048, blank=True)
    director = models.CharField(max_length=512, blank=True)
    producer = models.CharField(max_length=512, blank=True)
    release_date = models.CharField(max_length=512, blank=True)
    rt_score = models.CharField(max_length=512, blank=True)
    people = models.ManyToManyField(People)

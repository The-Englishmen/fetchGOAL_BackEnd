from rest_framework import serializers
from django.db import models


# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    league = models.For

    def __str__(self):
        return self.league

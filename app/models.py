from django.db import models


# Create your models here.


class Federation(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return f'{self.name},{self.photo_url}'

class League(models.Model):
    name = models.CharField(max_length=100)
    federation = models.ForeignKey(Federation, on_delete=models.CASCADE, related_name='leagues', null=True)
    photo_url = models.TextField()

    def __str__(self):
        return f'{self.name},{self.federation},{self.photo_url}'


class Team(models.Model):
    name = models.CharField(max_length=100)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')
    photo_url = models.TextField(default=None)


    def __str__(self):
        return f'{self.name},{self.league},{self.photo_url}'

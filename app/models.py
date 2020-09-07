from django.db import models


# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=100)
    federation = models.ForeignKey(Federation, on_delete=models.CASCADE, related_name='federation')
    photo_url = models.TextField()

    def __str__(self):
        return f'{self.name},{self.federation}''


class Team(models.Model):
    name = models.CharField(max_length=100)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')
    preview_url = models.CharField(max_length=200, null=True)


    def __str__(self):
        return f'{self.name},{self.league},{self.preview_url}'

class Federation(models.Model):
    name = models.CharField(max_length=100)
    preview_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name},{self.preview_url}'
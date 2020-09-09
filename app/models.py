from django.db import models


# Create your models here.


class Federation(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class League(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()
    federation = models.ForeignKey(Federation, on_delete=models.CASCADE, related_name='leagues')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')
    federation = models.ForeignKey(Federation, on_delete=models.CASCADE, related_name='teams')
    photo_url = models.TextField()


    def __str__(self):
        return self.name

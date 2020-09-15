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


class Tournament(models.Model):
    name = models.CharField(max_length=100)
<<<<<<< HEAD
    federation = models.ForeignKey(Federation, on_delete=models.CASCADE, related_name='tournaments')
=======
    federation = models.ForeignKey(Federation, on_delete=models.CASCADE, related_name='tournament')
>>>>>>> dev
    photo_url = models.TextField()


    def __str__(self):
<<<<<<< HEAD
        return self.name


class Championship(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='championships')
    federation = models.ForeignKey(Federation, on_delete=models.CASCADE, related_name='championships')
    photo_url = models.TextField()


    def __str__(self):
        return self.name
=======
        return self.name
>>>>>>> dev

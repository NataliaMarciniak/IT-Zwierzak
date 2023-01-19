from django.db import models

class Announcement(models.Model):
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    name = models.CharField(max_length=15)
    age = models.SmallIntegerField(20)
    health = models.TextField()
    description = models.TextField()

class ButtonQuestion(models.Model):
    button = models.ForeignKey(Announcement, on_delete=models.CASCADE)

from django.db import models


class Announcement(models.Model):
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    name = models.CharField(max_length=15)
    age = models.SmallIntegerField()
    health = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.species} {self.name} - {self.age} lat'


class ButtonQuestion(models.Model):
    button = models.ForeignKey(Announcement, on_delete=models.CASCADE)


class Member(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}'

from django.conf import settings
from django.db import models


class Announcment(models.Model):
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    name = models.CharField(max_length=15)

    health = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.species} {self.name} - {self.age} lat'


class Animal(models.Model):
    GENDER_CHOICES = [
        ('M', 'Męska'),
        ('F', 'Żeńska'),
        ('O', 'Inna')]

    SPECIES_CHOICES = [
        ('dog', 'Pies'),
        ('cat', 'Kot'),
        ('rabbit', 'Królik'),
        ('snake', 'Wonsz'),
        ('other', 'Inne')
    ]

    species = models.CharField(choices=SPECIES_CHOICES, default='dog', max_length=10)  # TODO choice variable shows in En
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    name = models.CharField(max_length=20)
    color = models.CharField(max_length=100)
    weight = models.FloatField(max_length=10, help_text='w kilogramach')

    age = models.PositiveSmallIntegerField()
    months = models.PositiveSmallIntegerField(help_text='fill when age is below 1 year', default=0)

    image = models.ImageField(null=True, blank=True, upload_to="images/")

    health_and_vaccination = models.TextField(default=' ', max_length=3000, null=True, blank=True)
    care = models.TextField(default=' ', max_length=3000, null=True, blank=True)
    past = models.TextField(default=' ', max_length=3000, null=True, blank=True)

    care_taker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True}
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.species} {self.name} - {self.age}'

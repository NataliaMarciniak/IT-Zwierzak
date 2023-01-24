from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Announcement(models.Model):
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    name = models.CharField(max_length=15)
    health = models.CharField(max_length=30)
    short_description = models.TextField(max_length=300, default=' ')
    description = models.TextField(max_length=300)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.species} {self.name} - {self.age} lat'

class AdoptionApplication(models.Model):
    your_education = models.CharField(max_length=250)

    number_of_adults_in_the_house = models.PositiveSmallIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(10),
    ])

    number_of_children_in_the_house = models.PositiveSmallIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(10),
    ])

    other_animals = models.CharField(max_length=250)

    hours_away_from_home = models.PositiveSmallIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(12),
    ])

    moving_out = models.CharField(max_length=250)

    family_allergies = models.CharField(max_length=250)

    adoption_reason = models.CharField(max_length=250)

    animal_name = models.CharField(max_length=50)

    availability = models.PositiveSmallIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(24),
    ])

    feeding_the_animal = models.CharField(max_length=250)

    care_budget = models.CharField(max_length=150)

    what_if_you_go_on_vacation = models.CharField(max_length=250)

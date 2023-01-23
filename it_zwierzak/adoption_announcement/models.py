from django.core.validators import MaxValueValidator, MinValueValidator, ValidationError
from django.db import models


class Announcement(models.Model):
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    name = models.CharField(max_length=15)

    health = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.species} {self.name} - {self.age} lat'

class AdoptionApplication(models.Model):
    your_education = models.CharField(max_length=250)

    number_of_adults_in_the_house = models.PositiveSmallIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(10),
    ])
    # number_of_children_in_the_house = models.CharField(choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)), max_length=1, default=0)

    number_of_children_in_the_house = models.PositiveSmallIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(10),
    ])

    other_animals = models.CharField(max_length=250)

    hours_away_from_home = models.PositiveSmallIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(12),
    ])

    what_about_moving = models.CharField(max_length=300)

    someone_is_allergic = models.CharField(max_length=250)

    why_adoption = models.CharField(max_length=250)

    specific_animal_to_adopt = models.CharField(max_length=250)

    hours_of_interaction = models.PositiveSmallIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(24),
    ])

    feeding_the_animal = models.CharField(max_length=250)

    animal_maintenance = models.CharField(max_length=250)

    what_if_you_go_on_vacation = models.CharField(max_length=250)

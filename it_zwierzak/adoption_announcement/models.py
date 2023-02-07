from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Announcement(models.Model):
    animal = models.OneToOneField('Animal', on_delete=models.CASCADE)
    short_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True}, null=True
    )

    def __str__(self):
        return f'{self.animal.name}'


class Animal(models.Model):
    GENDER_CHOICES = [
        ('Samiec', 'Samiec'),
        ('Samica', 'Samica'),
        ('Inna', 'Inna')]

    species = models.CharField(max_length=10)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Inna')
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=100)
    weight = models.FloatField(max_length=10, help_text='w kilogramach', validators=[MinValueValidator(0.1)])
    age = models.PositiveSmallIntegerField()
    months = models.PositiveSmallIntegerField(help_text='fill when age is below 1 year', default=0,
                                              validators=[MaxValueValidator(12)], null=True, blank=True
                                              )
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    health_and_vaccination = models.TextField(null=True, blank=True)
    history = models.TextField(null=True, blank=True)
    care_taker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True}
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.species} {self.name} - {self.age}'


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
    care_budget = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(24),
    ])
    what_if_you_go_on_vacation = models.CharField(max_length=250)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.applicant.username} {self.animal}'

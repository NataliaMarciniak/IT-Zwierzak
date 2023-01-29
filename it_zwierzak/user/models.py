from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=17)
    street = models.CharField(max_length=16)
    house_number = models.CharField(max_length=6)
    apartment_number = models.CharField(max_length=6)
    postcode = models.CharField(max_length=6)
    city = models.CharField(max_length=16)

    def __str__(self):
        return str(self.user)

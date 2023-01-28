from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    phone_number = models.IntegerField()
    street = models.CharField(max_length=16)
    house_number = models.IntegerField()
    apartment_number = models.IntegerField()
    postcode = models.IntegerField()
    city = models.CharField(max_length=16)

    def __str__(self):
        return str(self.user)

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed


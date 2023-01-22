from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User #add this

# Create your models here.
 ...

class Profile(models.Model):   #add this class and the following fields
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product)
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields here
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    address = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.

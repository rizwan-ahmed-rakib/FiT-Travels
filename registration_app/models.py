from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    USER = 'user'
    ADMIN = 'admin'
    SUPERUSER = 'superuser'

    PRIVILEGE_CHOICES = [
        (USER, 'User'),
        (ADMIN, 'Admin'),
        (SUPERUSER, 'Superuser'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    privileges = models.CharField(
        max_length=10,
        choices=PRIVILEGE_CHOICES,
        default=USER,
    )
    picture = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.full_name

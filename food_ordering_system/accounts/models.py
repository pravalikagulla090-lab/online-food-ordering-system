from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('restaurant', 'Restaurant Owner'),
        ('delivery', 'Delivery Person'),
        ('admin', 'Admin'),
    )
    email = models.EmailField(unique=True) # [cite: 2]
    phone = models.CharField(max_length=15, blank=True, null=True) # [cite: 3]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='customer') # [cite: 3]

    REQUIRED_FIELDS = ['email', 'role'] # [cite: 3]
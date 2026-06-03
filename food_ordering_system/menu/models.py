from django.db import models
from django.conf import settings

class Restaurant(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='menu_restaurants', null=True, blank=True)
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True)
    address = models.TextField(null=True, blank=True)  # 🌟 Added null/blank
    contact = models.CharField(max_length=50, null=True, blank=True)  # 🌟 Added null/blank

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_veg = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)

    def __str__(self):
        return self.name
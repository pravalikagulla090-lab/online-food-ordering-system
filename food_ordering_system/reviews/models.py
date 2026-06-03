from django.db import models
from django.contrib.auth import get_user_model
from menu.models import Restaurant

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_reviews')
    rating = models.PositiveIntegerField() 
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating} Stars by {self.user.username}"
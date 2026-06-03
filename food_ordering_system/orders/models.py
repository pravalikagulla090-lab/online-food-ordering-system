from django.db import models
from django.conf import settings
from menu.models import MenuItem

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='orders',
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order {self.id} by User {self.user_id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x Item for Order {self.order.id}"
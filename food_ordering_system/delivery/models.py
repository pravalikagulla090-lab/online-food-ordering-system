from django.db import models
from django.contrib.auth import get_user_model
from orders.models import Order # [cite: 23]

User = get_user_model()

class DeliveryAgent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # [cite: 23]
    is_available = models.BooleanField(default=True) # [cite: 23]
    vehicle_number = models.CharField(max_length=50, blank=True) # [cite: 23]

    def __str__(self):
        return self.user.username # [cite: 23]

class DeliveryTracking(models.Model):
    DELIVERY_STATUS = [
        ('ASSIGNED', 'Assigned to Agent'), # [cite: 23]
        ('PICKED_UP', 'Picked Up from Restaurant'), # [cite: 23]
        ('NEARBY', 'Arriving Soon'), # [cite: 23]
        ('DELIVERED', 'Delivered Successfully'), # [cite: 23]
    ]
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='delivery_info') # [cite: 23]
    agent = models.ForeignKey(DeliveryAgent, on_delete=models.SET_NULL, null=True, blank=True) # [cite: 24]
    status = models.CharField(max_length=20, choices=DELIVERY_STATUS, default='ASSIGNED') # [cite: 24]
    estimated_delivery_time = models.DateTimeField(null=True, blank=True) # [cite: 24]
    updated_at = models.DateTimeField(auto_now=True) # [cite: 24]

    def __str__(self):
        return f"Delivery Tracking for Order #{self.order.id} - {self.status}" # [cite: 24]
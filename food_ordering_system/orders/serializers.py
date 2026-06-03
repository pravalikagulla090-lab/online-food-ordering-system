from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__' # [cite: 50]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True) # [cite: 50]
    total_price = serializers.CharField(source='total_amount', read_only=True) # JavaScript template fallback mapping [cite: 372]

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'status', 'total_amount', 'total_price', 'items'] # [cite: 50]
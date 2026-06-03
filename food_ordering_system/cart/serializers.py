from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    item_name = serializers.ReadOnlyField(source='menu_item.name')  
    item_price = serializers.ReadOnlyField(source='menu_item.price')      
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'menu_item', 'item_name', 'item_price', 'quantity', 'subtotal']

    def get_subtotal(self, obj):
        try:
            return obj.quantity * float(obj.menu_item.price)
        except (TypeError, ValueError, AttributeError):
            return 0.0
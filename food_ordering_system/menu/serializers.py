from rest_framework import serializers
from .models import Restaurant, Category, MenuItem

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'category_name']

class MenuItemSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(source='name', read_only=True)
    category_title = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'restaurant', 'category', 'name', 'food_name', 'description', 'price', 'is_veg', 'category_title', 'image']

class RestaurantSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)
    restaurant_name = serializers.CharField(source='name', read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'owner', 'name', 'restaurant_name', 'description', 'address', 'contact', 'menu_items']
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Restaurant, Category, MenuItem
from .serializers import RestaurantSerializer, CategorySerializer, MenuItemSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.AllowAny]

    # 🌟 FIXED: Explicitly wrap the list data in a 'results' key to match your HTML fetch code!
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "results": serializer.data
        })

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('title')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class MenuItemViewSet(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        restaurant_id = self.request.query_params.get('restaurant')
        if restaurant_id is not None:
            queryset = queryset.filter(restaurant_id=restaurant_id)
        return queryset
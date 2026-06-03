from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, CategoryViewSet, MenuItemViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='api-restaurants')
router.register(r'categories', CategoryViewSet, basename='api-categories')
router.register(r'menu', MenuItemViewSet, basename='api-menu-items')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', RestaurantViewSet.as_view({'get': 'retrieve'}), name='api-restaurant-nested'),
]
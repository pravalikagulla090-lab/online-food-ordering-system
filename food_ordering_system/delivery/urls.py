from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeliveryTrackingViewSet

router = DefaultRouter()
router.register(r'tracking', DeliveryTrackingViewSet, basename='delivery-tracking') # [cite: 25]

urlpatterns = [
    path('', include(router.urls)),
]
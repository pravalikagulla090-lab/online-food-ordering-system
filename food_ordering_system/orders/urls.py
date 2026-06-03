from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'orders', views.OrderViewSet, basename='api-orders')

urlpatterns = [
    path('', include(router.urls)),
    path('confirm/', views.confirm_order, name='confirm_order'), # [cite: 51]
    path('cancel/', views.cancel_order, name='cancel_order'), # [cite: 51]
    path('cancel/<int:order_id>/', views.CancelOrderAPIView.as_view(), name='cancel_order_api'),
]
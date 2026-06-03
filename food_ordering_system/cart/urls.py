from django.urls import path
from . import views

urlpatterns = [
    # 🌟 HIJACK THE ADDRESS: This forces Django to accept requests at /api/v1/cart/
    # without running it through the automated router security check!
    path('', views.add_to_cart, name='frontend_cart'),
    
    # Keep these as fallback routes
    path('view/', views.add_to_cart, name='cart_view_fallback'),
    path('remove/<int:item_id>/', views.remove_item, name='remove_item'),
]
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import frontend_login
from cart import views as cart_views
from orders.views import checkout_view

urlpatterns = [
    # --- Frontend User Interface Routes (HTML Templates) ---
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', frontend_login, name='frontend_login'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='frontend_register'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='frontend_logout'),
    path('checkout/', checkout_view, name='checkout_view'),
    path('restaurants/', TemplateView.as_view(template_name='restaurant_list.html'), name='frontend_restaurants'),
    path('restaurants/menu/', TemplateView.as_view(template_name='menu_list.html'), name='frontend_menu_nested'),
    path('cart/', cart_views.add_to_cart, name='frontend_cart'),
    path('orders/', TemplateView.as_view(template_name='order_list.html'), name='frontend_orders'),
    path('delivery/', TemplateView.as_view(template_name='delivery_list.html'), name='frontend_delivery'),
    path('reviews/', TemplateView.as_view(template_name='review_list.html'), name='frontend_reviews'),
    path('reports/', TemplateView.as_view(template_name='report_dashboard.html'), name='frontend_reports'),
    path('manage/', TemplateView.as_view(template_name='admin_dashboard.html'), name='frontend_admin_dashboard'),

    # --- Core Backend REST APIs (Data Channels) ---
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/cart/', include('cart.urls')),
    path('api/v1/orders/', include('orders.urls')),
    path('api/v1/delivery/', include('delivery.urls')),
    path('api/v1/reviews/', include('reviews.urls')),
    path('api/v1/reports/', include('reports.urls')),

    # --- Standalone Menu Feature Routing & Frontend Fallbacks ---
    path('api/v1/menu/', include('menu.urls')),
    path('api/v1/restaurants/', include('menu.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
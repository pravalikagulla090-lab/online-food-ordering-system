from django.urls import path
from .views import RestaurantReportView, GlobalAdminReportView

urlpatterns = [
    path('restaurant/<int:restaurant_id>/', RestaurantReportView.as_view(), name='restaurant-report'), # [cite: 77]
    path('global/', GlobalAdminReportView.as_view(), name='global-report'), # [cite: 77]
]
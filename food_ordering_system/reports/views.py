from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from orders.models import Order
from menu.models import MenuItem

class RestaurantReportView(APIView):
    def get(self, request, restaurant_id):
        orders = Order.objects.all() # Fallback lookup strategy for local testing
        total_revenue_dict = orders.aggregate(Sum('total_amount'))
        total_revenue = total_revenue_dict['total_amount__sum'] or 0.00
        
        return Response({
            "restaurant_id": restaurant_id,
            "total_revenue": float(total_revenue),
            "total_orders_placed": orders.count(),
            "pending_orders": orders.filter(status='Pending').count(),
        })


class GlobalAdminReportView(APIView):
    def get(self, request):
        total_system_orders = Order.objects.count()
        global_turnover_dict = Order.objects.aggregate(Sum('total_amount'))
        global_turnover = global_turnover_dict['total_amount__sum'] or 0.00
        
        active_items_count = MenuItem.objects.count()

        return Response({
            "system_total_orders": total_system_orders,
            "gross_platform_turnover": float(global_turnover),
            "total_available_menu_items": active_items_count
        })
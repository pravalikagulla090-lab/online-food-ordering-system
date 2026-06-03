from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer
from django.utils.decorators import method_decorator  # 🌟 ADD THIS IMPORT AT THE TOP
from django.views.decorators.csrf import csrf_exempt

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]


@login_required(login_url='frontend_login')
def confirm_order(request):
    if request.method == "POST":
        cart = getattr(request.user, 'cart', None)
        cart_items = cart.items.all() if cart else []

        if not cart_items:
            messages.error(request, "Your cart is empty!")
            return redirect('frontend_cart')

        calculated_grand_total = sum(item.quantity * item.menu_item.price for item in cart_items)

        order = Order.objects.create(
            user=request.user,
            status="Pending",
            total_amount=calculated_grand_total
        )
        
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                menu_item=item.menu_item,
                quantity=item.quantity,
                price=item.menu_item.price
            )

        cart_items.delete()
        messages.success(request, "🎉 Your order has been confirmed successfully!")
        return redirect('frontend_orders')


@login_required(login_url='frontend_login')
def cancel_order(request):
    if request.method == "POST":
        cart = getattr(request.user, 'cart', None)
        if cart:
            cart.items.all().delete()
        messages.warning(request, "🗑️ Your pending checkout was cancelled and your cart has been emptied.")
        return redirect('frontend_restaurants')


# 🌟 1. CREATE A CUSTOM AUTHENTICATION CLASS THAT BYPASSES CSRF ENFORCEMENT
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # Do nothing! This completely turns off the CSRF check for this session.

# 🌟 1. DEFINE THE BYPASS AUTHENTICATION LAYER RIGHT ABOVE YOUR VIEW
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # This completely disables the strict DRF CSRF check for your browser session

# 🌟 2. APPLY THE DECORATOR AND THE CUSTOM CLASS TOGETHER
@method_decorator(csrf_exempt, name='dispatch')
class CancelOrderAPIView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, order_id):
        order = Order.objects.filter(id=order_id, user=request.user).first()
        if not order:
            return Response({'detail': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        if order.status in ['Completed', 'Out for Delivery']:
            return Response({'detail': 'Cannot cancel an order that is already out for delivery or completed.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if order.status == 'Cancelled':
            return Response({'detail': 'Order is already cancelled.'}, status=status.HTTP_400_BAD_REQUEST)
            
        order.status = 'Cancelled'
        order.save()
        return Response({'detail': 'Order cancelled successfully.', 'order_id': order.id, 'status': order.status}, status=status.HTTP_200_OK)
    
@login_required(login_url='frontend_login')
def checkout_view(request):
    cart = getattr(request.user, 'cart', None)
    cart_items = cart.items.all() if cart else []
    subtotal = 0
    for item in cart_items:
        item.total_price = item.quantity * item.menu_item.price
        subtotal += item.total_price
    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
    })

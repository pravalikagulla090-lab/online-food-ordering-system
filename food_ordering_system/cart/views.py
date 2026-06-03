from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse
from menu.models import MenuItem
from .models import Cart, CartItem

@csrf_exempt
def add_to_cart(request, item_id=None):
    if not request.user.is_authenticated:
        if request.content_type == 'application/json' or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'detail': 'Authentication required'}, status=401)
        login_url = f"{reverse('frontend_login')}?next={request.path}"
        return redirect(login_url)

    cart, created = Cart.objects.get_or_create(user=request.user)

    # 1. If the browser is trying to ADD an item (POST)
    if request.method == 'POST':
        import json
        target_id = item_id or request.POST.get('item_id')

        # If cache sends it via old JSON format, catch it safely
        if not target_id and request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
                target_id = data.get('menu_item_id') or data.get('item_id')
            except json.JSONDecodeError:
                pass

        if target_id:
            menu_item = get_object_or_404(MenuItem, id=target_id)
            cart_item, item_created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)
            if not item_created:
                cart_item.quantity += 1
                cart_item.save()

            # If it's an AJAX fetch, send success JSON to clear alerts
            if request.content_type == 'application/json':
                return JsonResponse({"status": "success", "message": "Item added successfully"})
            
            # If it's a traditional form, reload into the cart view layout
            return redirect('/cart/')

    # 2. If the user is just looking at the cart page (GET)
    if hasattr(cart, 'items'):
        cart_items = cart.items.all()
    else:
        cart_items = cart.cartitem_set.all()

    subtotal = 0
    for item in cart_items:
        item.total_price = item.quantity * item.menu_item.price
        subtotal += item.total_price

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
    }
    return render(request, 'cart_list.html', context)

@csrf_exempt
@login_required(login_url='frontend_login')
def remove_item(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart_item.delete()
    return redirect('/api/v1/cart/')
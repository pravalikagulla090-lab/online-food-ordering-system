from django.contrib import admin
from .models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)

#from .models import Delivery, Review
#admin.site.register(Delivery)
#admin.site.register(Review)
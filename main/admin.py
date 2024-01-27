from django.contrib import admin
from .models import Company, Coupon, CartItem

admin.site.register(Coupon)
admin.site.register(Company)
admin.site.register(CartItem)

from django.contrib import admin
from .models import CartItem, Order

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'added_at']
    list_filter = ['user', 'product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'is_paid']
    list_filter = ['is_paid', 'created_at']

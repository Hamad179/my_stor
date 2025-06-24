from django.contrib import admin
from .models import CustomerProfile

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone', 'address']
    search_fields = ['user__username', 'phone']

# my_stor/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('cart/', include('cart.urls')),  # يتضمن cart1/
    path('customers/', include('customers.urls')),
]

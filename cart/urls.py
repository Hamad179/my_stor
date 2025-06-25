# cart/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cart1/', views.cart_view, name='cart1'),
]

# cart/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('cart1/', views.cart_view, name='cart1'),
    path('login/', auth_views.LoginView.as_view(template_name='cart/login.html'), name='login'),
    path('reset-password/', views.reset_password_view, name='reset-password'),
    path('register/', views.register_view, name='register'),
    path('about/', views.about_view, name='about'),
]

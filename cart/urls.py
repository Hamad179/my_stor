# cart/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import profile_view
from .views import logout_view


urlpatterns = [
    path('cart1/', views.cart_view, name='cart1'),
    path('login/', auth_views.LoginView.as_view(template_name='cart/login.html'), name='login'),
    path('reset-password/', views.reset_password_view, name='reset-password'),
    path('register/', views.register_view, name='register'),
    path('about/', views.about_view, name='about'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('cart/', views.cart_view, name='cart'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='customers-profile'),
]

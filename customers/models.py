from django.db import models
from django.contrib.auth.models import User

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="رقم الجوال")
    address = models.TextField(blank=True, null=True, verbose_name="العنوان")

    def __str__(self):
        return self.user.username

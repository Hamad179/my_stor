from django.db import models
from store.models import Product
from django.contrib.auth.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)  # حقل لتاريخ الإضافة

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="العميل")
    items = models.ManyToManyField('CartItem')  # إصلاح الاستخدام
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False, verbose_name="تم الدفع؟")

    added_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"طلب #{self.id} - {self.user.username}"

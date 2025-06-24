from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم القسم")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم المنتج")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="القسم")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="صورة المنتج")
    available = models.BooleanField(default=True, verbose_name="متوفر؟")

    def __str__(self):
        return self.name

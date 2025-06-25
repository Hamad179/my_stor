# cart/views.py

from django.shortcuts import render

def cart_view(request):
    # قائمة مؤقتة - لاحقًا يمكن ربطها بـ session
    cart_items = [
        {"name": "منتج 1", "price": 99},
        {"name": "منتج 2", "price": 129},
    ]
    return render(request, "cart/cart1.html", {"cart_items": cart_items})

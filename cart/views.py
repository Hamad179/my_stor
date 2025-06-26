# cart/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def cart_view(request):
    # قائمة مؤقتة - لاحقًا يمكن ربطها بـ session
    cart_items = [
        {"name": "منتج 1", "price": 99},
        {"name": "منتج 2", "price": 129},
    ]
    return render(request, "cart/cart1.html", {"cart_items": cart_items})


def reset_password_view(request):
    if request.method == 'POST':
        # معالجة البريد الإلكتروني أو الطباعة فقط للتجربة
        email = request.POST.get('email')
        print(f"طلب إعادة تعيين من: {email}")
    return render(request, 'cart/reset_password.html')



def register_view(request):
    if request.method == 'POST':
        # البيانات المرسلة من النموذج
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"تم طلب إنشاء حساب: {username} - {email}")
        # لاحقًا يمكن إضافة إنشاء مستخدم فعلي
    return render(request, 'cart/register.html')


def about_view(request):
    return render(request, 'cart/about.html')


@login_required
def profile_view(request):
    return render(request, 'cart/profile.html')
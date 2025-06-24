from django.http import HttpResponse

def view_cart(request):
    return HttpResponse("هذه صفحة السلة")

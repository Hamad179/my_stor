from django.http import HttpResponse

def profile(request):
    return HttpResponse("هذه صفحة حساب العميل")

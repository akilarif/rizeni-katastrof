from django.shortcuts import render

# Create your views here.
def login_register(request):
    return render(request, 'disasterApp/login_register.html', {})

from django.shortcuts import render

# Create your views here.
def login_register(request):
    return render(request, 'disasterApp/login_register.html', {})

def user_page(request):
	return render(request, 'disasterApp/user_page.html', {})

def register(request):
	return render(request, 'disasterApp/register.html', {})

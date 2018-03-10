from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
# Create your views here.
def login_register(request):
    return render(request, 'disasterApp/login_register.html', {})

def user_page(request):
	return render(request, 'disasterApp/user_page.html', {})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            name=userObj['name']
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            emergency_contact_name=userObj['emergency_contact_name']
            emergency_contact_email=userObj['emergency_contact_email']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that username or email already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'disasterApp/register.html', {'form' : form})

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
#from .forms import UserRegistrationForm
from .forms import SignUpForm


# Create your views here.
def login_register(request):
    return render(request, 'disasterApp/login_register.html', {})

def user_page(request):
	return render(request, 'disasterApp/user_page.html', {})
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.location=form.cleaned_data.get('location')
            user.profile.name=form.cleaned_data.get('name')
            user.profile.gender=form.cleaned_data.get('gender')
            user.profile.email=form.cleaned_data.get('email')
            user.profile.emergency_contact=form.cleaned_data.get('emergency_contact')
            user.profile.emergency_email=form.cleaned_data.get('emergency_email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/user_page/')
    else:
        form = SignUpForm()
    return render(request, 'disasterApp/register.html', {'form': form})


"""
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
"""
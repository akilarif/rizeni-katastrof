from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from disasterApp.models import *
#from .forms import UserRegistrationForm
from .forms import SignUpForm
import urllib.request
import json
from geopy.geocoders import Nominatim
from .forms import Missing_Form


# Create your views here.
def login_register(request):
    return render(request, 'disasterApp/login_register.html', {})

def user_page(request):
    form=Missing_Form(request.POST)
    city = Profile.objects.get(user = request.user).location
    geolocator = Nominatim()
    location = geolocator.geocode(city)
    location=(location.latitude, location.longitude)
    location_str = str(location[0]) + "," + str(location[1])
    places = {}
    services = ["hospital", "pharmacy", "police", "atm", "fire_station", "gas_station"]
    for service in services:
        place = []
        url = ("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + location_str +
                "&radius=500&type=" + service + "&key=AIzaSyDbh2MphtWNNOPKdhueje18_9oebLZFl4A")
        with urllib.request.urlopen(url) as u:
            result = json.loads(u.read().decode())
            place_objs = result["results"]
            for place_obj in place_objs:
                place_tuple = (place_obj["name"], place_obj["vicinity"], place_obj["geometry"]["location"])
                place.append(place_tuple)
            places[service] = place
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/missing_people/')
    else:
        return render(request, 'disasterApp/user_page.html', {"places": places,"form":form})
	
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
            user.profile.contact_no=form.cleaned_data.get('contact_no')
            user.profile.emergency_no=form.cleaned_data.get('emergency_no')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/user_page/')
    else:
        form = SignUpForm()
    return render(request, 'disasterApp/register.html', {'form': form})






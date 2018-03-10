#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 12:35:07 2018

@author: satyam


from django import forms
class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
    
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    location = forms.CharField(
        required = True,
        label = 'location',
        max_length = 32
    )
    name= forms.CharField(max_length=32, required=True)
    location = forms.CharField(max_length=32)
    birth_date = forms.DateField()
    gender=forms.CharField(max_length=8)
    email=forms.EmailField(max_length=256, required=True)
    emergency_contact_name= forms.CharField(max_length=32, required=True)
    emergency_email=forms.EmailField(max_length=256, required=True)
    

    class Meta:
        model = User
        fields = ('username','name','gender', 'birth_date','email', 'password1', 'password2', 'location' ,'emergency_contact_name','emergency_email' )
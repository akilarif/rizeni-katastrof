#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 12:35:07 2018

@author: satyam
"""

from django import forms
class UserRegistrationForm(forms.Form):
    name = forms.CharField(
        required = True,
        label = 'Name',
        max_length = 32
    )
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
    emergency_contact_name=forms.CharField(
        required = True,
        label = 'Emergency Contact Name',
        max_length = 32
    )
    emergency_contact_email=forms.CharField(
        required = True,
        label = 'Emergency Contact Email',
        max_length = 32,
    )
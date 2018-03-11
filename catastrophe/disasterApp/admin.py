from django.contrib import admin
from .models import Profile
from .models import Missing_Person
# Register your models here.
admin.site.register(Profile)
admin.site.register(Missing_Person)
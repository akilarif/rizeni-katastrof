from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.login_register, name='login_register'),
]
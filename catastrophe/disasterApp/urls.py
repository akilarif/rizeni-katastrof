from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.login_register, name='login_register'),
    url(r'^user_page/', views.user_page, name='user_page'),
    url(r'^register/', views.register, name='register'),
]
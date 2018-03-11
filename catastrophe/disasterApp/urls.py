from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'disasterApp/login_register.html'}),
    url(r'^user_page/', views.user_page, name='user_page'),
    url(r'^register/', views.register, name='register'),
    url(r'^notifications/', views.notifications, name='notifications'),
    url(r'^logout/$', auth_views.logout),
]
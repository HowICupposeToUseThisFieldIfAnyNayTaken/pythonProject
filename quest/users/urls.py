from django.template.defaulttags import url
from django.urls import path, include
from . import views
from .views import Register
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('profile', views.profile, name='profile'),
    path('register', Register.as_view(), name='register'),
    #url(r'^login/$', views.login,name='login'),
]
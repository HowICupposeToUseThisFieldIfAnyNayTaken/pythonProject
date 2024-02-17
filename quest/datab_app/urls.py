from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.datab_view,name='datab_view'),
    path('sort',views.datab_sort,name='datab_sort'),
]

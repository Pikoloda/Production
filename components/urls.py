from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path("", views.all_components, name='all_components')
]
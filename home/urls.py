"""
urls.py
Reagan Zierke <reaganzierke@gmail.com>
12-03-2024
Creates the url for the home page of the site.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
]
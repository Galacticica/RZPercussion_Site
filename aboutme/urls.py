"""
urls.py
Reagan Zierke <reaganzierke@gmail.com>
12-03-2024
Creates the url for the about me part of the site.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
]
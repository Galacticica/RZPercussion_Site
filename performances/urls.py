"""
urls.py
Reagan Zierke <reaganzierke@gmail.com>
12-04-2024
Creates the urls for the performances part of the site. The slug field is also autogenerated here.
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="rz_performance_index"),

    path("<slug:slug>/", views.performance, name="performance"),

]
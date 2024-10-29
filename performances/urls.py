from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="rz_performance_index"),

    path("<slug:slug>/", views.performance, name="performance"),
    
]
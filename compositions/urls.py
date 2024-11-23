from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="rz_composition_index"),
    path("<slug:slug>/", views.composition, name="composition"),
]
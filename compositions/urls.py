from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.index, name="rz_composition_index"),
    path("<slug:slug>/", views.composition, name="composition"),
=======

>>>>>>> 4540dafd65d6c3bf004e0f13fb7c9de3bb54af69
]
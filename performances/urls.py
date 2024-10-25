from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("<int:performed_piece_id>/", views.performance, name="performance")
]
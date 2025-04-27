from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    path("", views.home, name="home"),
    path("plants/", views.plant_index, name="plant-index"),
    path("about/", views.about, name="about"),
]

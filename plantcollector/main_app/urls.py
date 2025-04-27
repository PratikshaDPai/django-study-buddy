from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    path("", views.home, name="home"),
    path("plants/", views.list_plants, name="list_plants"),
    path("about/", views.about, name="about"),
]

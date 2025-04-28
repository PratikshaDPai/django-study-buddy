from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    path("", views.home, name="home"),
    path("plants/", views.plant_index, name="plant-index"),
    path("about/", views.about, name="about"),
    path("plants/<int:plant_id>/", views.plant_detail, name="plant-detail"),
    path("plants/create/", views.PlantCreate.as_view(), name="plant-create"),
    path("plants/<int:pk>/update/", views.PlantUpdate.as_view(), name="plant-update"),
    path("plants/<int:pk>/delete/", views.PlantDelete.as_view(), name="plant-delete"),
    path(
        "plants/<int:plant_id>/add-watering/", views.add_watering, name="add-watering"
    ),
]

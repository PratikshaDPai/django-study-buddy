from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("groups/", views.group_index, name="group-index"),
    path("about/", views.about, name="about"),
    path("groups/<int:group_id>/", views.group_detail, name="group-detail"),
    path("groups/create/", views.StudyGroupCreate.as_view(), name="group-create"),
    path(
        "groups/<int:pk>/update/", views.StudyGroupUpdate.as_view(), name="group-update"
    ),
    path(
        "groups/<int:pk>/delete/", views.StudyGroupDelete.as_view(), name="group-delete"
    ),
    path("groups/<int:group_id>/add-message/", views.add_message, name="add-message"),
    path("accounts/signup/", views.signup, name="signup"),
]

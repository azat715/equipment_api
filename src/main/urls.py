from django.urls import path

from main.views import health, EqptTypeListView, EqptListView, EqptView


app_name = "main"

urlpatterns = [
    path("health", health, name="health"),
    path("equipment/<int:pk>", EqptView.as_view(), name="health"),
    path("equipment", EqptListView.as_view(), name="equipment-list"),
    path("equipment-type", EqptTypeListView.as_view(), name="equipment-type"),
]

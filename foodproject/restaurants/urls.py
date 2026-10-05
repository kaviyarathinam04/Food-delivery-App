from django.urls import path
from . import views

urlpatterns = [
    path("", views.restaurant_list, name="restaurants"),
    path(
        "<slug:restaurant_id>/",
        views.restaurant_detail,
        name="restaurant_detail"
    ),
]
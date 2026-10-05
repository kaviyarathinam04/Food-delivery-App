from django.urls import path
from . import views


urlpatterns = [

    # Cart
    path("", views.cart_view, name="cart"),

    # Add item
    path(
        "add/<str:food_id>/",
        views.add_to_cart,
        name="add_to_cart"
    ),

    # Quantity
    path(
        "increase/<str:food_id>/",
        views.increase_quantity,
        name="increase"
    ),

    path(
        "decrease/<str:food_id>/",
        views.decrease_quantity,
        name="decrease"
    ),

    # Remove
    path(
        "remove/<str:food_id>/",
        views.remove_from_cart,
        name="remove"
    ),

    # Clear
    path(
        "clear/",
        views.clear_cart,
        name="clear"
    ),

    # Checkout
    path(
        "checkout/",
        views.checkout,
        name="checkout"
    ),

    # Order success
    path(
        "order-success/",
        views.order_success,
        name="order_success"
    ),
]
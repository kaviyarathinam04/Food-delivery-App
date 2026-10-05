from django.urls import path

from . import views


app_name = "orders"


urlpatterns = [

    path(
        "checkout/",
        views.checkout,
        name="checkout"
    ),

    path(
        "payment/",
        views.payment,
        name="payment"
    ),

    path(
        "success/",
        views.success,
        name="success"
    ),

    path(
        "invoice/",
        views.invoice,
        name="invoice"
    ),

    path(
        "my-orders/",
        views.my_orders,
        name="my_orders"
    ),

]
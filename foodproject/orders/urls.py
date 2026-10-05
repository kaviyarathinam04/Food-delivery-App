from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_orders, name="orders_home"),
    path("checkout/", views.checkout, name="checkout"),
    path("payment/", views.payment, name="payment"),
    path("success/", views.success, name="success"),
    path("invoice/<int:order_id>/", views.invoice, name="invoice"),
    path("my-orders/", views.my_orders, name="my_orders"),
]
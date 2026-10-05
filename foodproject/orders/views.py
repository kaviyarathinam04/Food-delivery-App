from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Order


@login_required(login_url="/users/login/")
def my_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "my_orders.html",
        {
            "orders": orders
        }
    )


@login_required(login_url="/users/login/")
def invoice(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        "invoice.html",
        {
            "order": order
        }
    )


def checkout(request):
    return render(request, "checkout.html")


def payment(request):
    return render(request, "payment.html")


def success(request):
    return render(request, "order_success.html")
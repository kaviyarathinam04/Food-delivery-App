from decimal import Decimal

from django.shortcuts import redirect, render

from .models import Order


def get_cart_total(cart):
    total = Decimal("0")

    for item in cart.values():
        price = Decimal(str(item.get("price", "0")))
        quantity = int(item.get("quantity", 1))

        total += price * quantity

    return total


def checkout(request):

    cart = request.session.get("foodie_cart", {})

    if not cart:
        return redirect("cart:view")

    total = get_cart_total(cart)

    if request.method == "POST":

        request.session["checkout_name"] = request.POST.get(
            "name",
            ""
        )

        request.session["checkout_phone"] = request.POST.get(
            "phone",
            ""
        )

        request.session["checkout_address"] = request.POST.get(
            "address",
            ""
        )

        return redirect("orders:payment")

    return render(
        request,
        "checkout.html",
        {
            "total": total
        }
    )


def payment(request):

    cart = request.session.get("foodie_cart", {})

    if not cart:
        return redirect("cart:view")

    total = get_cart_total(cart)

    if request.method == "POST":

        payment_method = request.POST.get(
            "payment_method",
            "COD"
        )

        order = Order.objects.create(

            user=(
                request.user
                if request.user.is_authenticated
                else None
            ),

            customer_name=request.session.get(
                "checkout_name",
                "Customer"
            ),

            phone=request.session.get(
                "checkout_phone",
                ""
            ),

            address=request.session.get(
                "checkout_address",
                ""
            ),

            payment_method=payment_method,

            total_amount=total,
        )

        request.session["last_order_id"] = order.id

        request.session["foodie_cart"] = {}

        request.session.modified = True

        return redirect("orders:success")

    return render(
        request,
        "payment.html",
        {
            "total": total
        }
    )


def success(request):

    order_id = request.session.get(
        "last_order_id"
    )

    order = None

    if order_id:

        try:
            order = Order.objects.get(
                id=order_id
            )

        except Order.DoesNotExist:
            order = None

    return render(
        request,
        "success.html",
        {
            "order": order
        }
    )


def invoice(request):

    order_id = request.session.get(
        "last_order_id"
    )

    order = None

    if order_id:

        try:
            order = Order.objects.get(
                id=order_id
            )

        except Order.DoesNotExist:
            order = None

    return render(
        request,
        "invoice.html",
        {
            "order": order
        }
    )


def my_orders(request):

    if request.user.is_authenticated:

        orders = Order.objects.filter(
            user=request.user
        ).order_by("-created_at")

    else:

        orders = []

    return render(
        request,
        "my_orders.html",
        {
            "orders": orders
        }
    )
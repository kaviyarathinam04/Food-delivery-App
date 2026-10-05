from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def restaurant(request):
    return render(request, "restaurant.html")


def menu(request):
    return render(request, "menu.html")


def cart(request):
    return render(request, "cart.html")


def checkout(request):
    return render(request, "checkout.html")


def payment(request):
    return render(request, "payment.html")


def success(request):
    return render(request, "success.html")


def invoice(request):
    return render(request, "invoice.html")


def my_orders(request):
    return render(request, "my_orders.html")


def login_page(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def offers(request):
    return render(request, "offers.html")
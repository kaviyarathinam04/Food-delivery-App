from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            next_url = request.GET.get("next")

            if next_url:
                return redirect(next_url)

            return redirect("/")

        return render(
            request,
            "login.html",
            {"error": "Invalid username or password"}
        )

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(
                request,
                "register.html",
                {"error": "Passwords do not match"}
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "register.html",
                {"error": "Username already exists"}
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect("/")

    return render(request, "register.html")


def offers(request):
    return render(request, "offers.html")
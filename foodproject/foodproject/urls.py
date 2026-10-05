"""
URL configuration for foodproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home
    path("", views.home, name="home"),

    # Restaurant
    path("restaurants/", include("restaurants.urls")),

    # Menu
    path("menu/", include("menu.urls")),

    # Cart
    path("cart/", include("cart.urls")),

    # Offers
    path("offers/", include("offers.urls")),

    # Login / Register
    path("users/", include("users.urls")),

    # Orders
    path("orders/", include("orders.urls")),
]
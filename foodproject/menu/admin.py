from django.contrib import admin

from .models import FoodItem


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "restaurant",
        "category",
        "price",
        "is_available",
    )

    list_filter = (
        "category",
        "restaurant",
        "is_available",
    )

    search_fields = (
        "name",
        "category",
    )
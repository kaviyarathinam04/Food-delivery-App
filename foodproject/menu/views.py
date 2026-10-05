from django.shortcuts import render

from restaurants.views import RESTAURANTS


def menu_home(request):

    all_foods = []

    for restaurant_id, restaurant in RESTAURANTS.items():

        for food in restaurant.get("foods", []):

            all_foods.append({
                "id": food["id"],
                "name": food["name"],
                "price": food["price"],
                "image": food["image"],
                "restaurant": restaurant["name"],
                "restaurant_id": restaurant_id,
                "category": restaurant["category"],
                "rating": restaurant["rating"],
            })

    return render(
        request,
        "menu.html",
        {
            "foods": all_foods,
        }
    )
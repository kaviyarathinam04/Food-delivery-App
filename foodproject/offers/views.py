from django.shortcuts import render


def offers_list(request):

    offers = [
        {
            "title": "FLAT ₹100 OFF",
            "description": "On selected food orders",
            "code": "FOOD100",
        },
        {
            "title": "20% OFF",
            "description": "On selected burger combos",
            "code": "BURGER20",
        },
        {
            "title": "FREE DELIVERY",
            "description": "On orders above ₹499",
            "code": "FREEDEL",
        },
    ]

    return render(
        request,
        "offers.html",
        {
            "offers": offers
        }
    )
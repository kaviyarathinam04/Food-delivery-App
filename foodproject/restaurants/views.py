from django.shortcuts import render


RESTAURANTS = {

    "a2b": {
        "name": "A2B",
        "category": "South Indian",
        "rating": "4.7",
        "time": "25-30 min",
        "price": "₹₹",
        "location": "Dindigul",
        "description": "Delicious South Indian food with authentic taste and quality ingredients.",
        "image": "https://images.unsplash.com/photo-1589302168068-964664d93dc0?auto=format&fit=crop&w=1200&q=85",

        "foods": [
            {
                "id": "a2b1",
                "name": "Idli Sambar",
                "price": 80,
                "image": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "a2b2",
                "name": "Masala Dosa",
                "price": 120,
                "image": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "a2b3",
                "name": "Paneer Dosa",
                "price": 160,
                "image": "https://images.unsplash.com/photo-1630383249896-424e482df921?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "a2b4",
                "name": "Poori Masala",
                "price": 100,
                "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "a2b5",
                "name": "Veg Meals",
                "price": 150,
                "image": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "a2b6",
                "name": "Paneer Rice",
                "price": 180,
                "image": "https://images.unsplash.com/photo-1601050690117-94f5f6fa8bd7?auto=format&fit=crop&w=900&q=85",
            },
        ],
    },


    "pizza-corner": {
        "name": "Pizza Corner",
        "category": "Pizza",
        "rating": "4.5",
        "time": "30-35 min",
        "price": "₹₹",
        "location": "Dindigul",
        "description": "Hot, cheesy and freshly baked pizzas made specially for you.",
        "image": "https://images.unsplash.com/photo-1579751626657-72bc17010498?auto=format&fit=crop&w=1200&q=85",

        "foods": [
            {
                "id": "pizza1",
                "name": "Classic Cheese Pizza",
                "price": 249,
                "image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "pizza2",
                "name": "Chicken Pizza",
                "price": 329,
                "image": "https://images.unsplash.com/photo-1579751626657-72bc17010498?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "pizza3",
                "name": "Veg Loaded Pizza",
                "price": 279,
                "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "pizza4",
                "name": "Farmhouse Pizza",
                "price": 299,
                "image": "https://images.unsplash.com/photo-1571407970349-bc81e7e96d47?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "pizza5",
                "name": "Paneer Pizza",
                "price": 289,
                "image": "https://images.unsplash.com/photo-1593560708920-61dd98c8a09c?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "pizza6",
                "name": "Mexican Pizza",
                "price": 319,
                "image": "https://images.unsplash.com/photo-1579751626657-72bc17010498?auto=format&fit=crop&w=900&q=85",
            },
        ],
    },


    "biryani-hub": {
        "name": "Biryani Hub",
        "category": "Biryani",
        "rating": "4.8",
        "time": "25-30 min",
        "price": "₹₹",
        "location": "Dindigul",
        "description": "Aromatic dum biryani prepared with authentic spices and tender meat.",
        "image": "https://images.unsplash.com/photo-1563379091339-03246963d96c?auto=format&fit=crop&w=1200&q=85",

        "foods": [
            {
                "id": "biryani1",
                "name": "Chicken Biryani",
                "price": 279,
                "image": "https://images.unsplash.com/photo-1563379091339-03246963d96c?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "biryani2",
                "name": "Mutton Biryani",
                "price": 349,
                "image": "https://images.unsplash.com/photo-1589302168068-964664d93dc0?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "biryani3",
                "name": "Egg Biryani",
                "price": 199,
                "image": "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "biryani4",
                "name": "Chicken 65",
                "price": 220,
                "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "biryani5",
                "name": "Mutton Sukka",
                "price": 299,
                "image": "https://images.unsplash.com/photo-1601050690117-94f5f6fa8bd7?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "biryani6",
                "name": "Grilled Chicken",
                "price": 299,
                "image": "https://images.unsplash.com/photo-1532550907401-a500c9a57435?auto=format&fit=crop&w=900&q=85",
            },
        ],
    },


    "burger-point": {
        "name": "Burger Point",
        "category": "Burger",
        "rating": "4.4",
        "time": "20-25 min",
        "price": "₹₹",
        "location": "Dindigul",
        "description": "Juicy burgers loaded with fresh vegetables, cheese and delicious sauces.",
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=1200&q=85",

        "foods": [
            {
                "id": "burger1",
                "name": "Chicken Burger",
                "price": 199,
                "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "burger2",
                "name": "Classic Cheese Burger",
                "price": 179,
                "image": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "burger3",
                "name": "Double Chicken Burger",
                "price": 249,
                "image": "https://images.unsplash.com/photo-1571091718767-18b5b1457add?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "burger4",
                "name": "Veg Burger",
                "price": 149,
                "image": "https://images.unsplash.com/photo-1520072959219-c595dc870360?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "burger5",
                "name": "Peri Peri Burger",
                "price": 219,
                "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "burger6",
                "name": "Cheese Fries",
                "price": 139,
                "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=900&q=85",
            },
        ],
    },


    "chinese-wok": {
        "name": "Chinese Wok",
        "category": "Chinese",
        "rating": "4.3",
        "time": "25-30 min",
        "price": "₹₹",
        "location": "Dindigul",
        "description": "Tasty Chinese favourites prepared fresh with authentic sauces and spices.",
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=1200&q=85",

        "foods": [
            {
                "id": "noodles1",
                "name": "Chicken Noodles",
                "price": 219,
                "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "noodles2",
                "name": "Veg Hakka Noodles",
                "price": 169,
                "image": "https://images.unsplash.com/photo-1612929633738-8fe44f7ec841?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "rice1",
                "name": "Chicken Fried Rice",
                "price": 229,
                "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "rice2",
                "name": "Veg Fried Rice",
                "price": 179,
                "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "chinese1",
                "name": "Chilli Chicken",
                "price": 249,
                "image": "https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "chinese2",
                "name": "Gobi Manchurian",
                "price": 199,
                "image": "https://images.unsplash.com/photo-1625398407796-82650a8c135f?auto=format&fit=crop&w=900&q=85",
            },
        ],
    },


    "shawarma-king": {
        "name": "Shawarma King",
        "category": "Shawarma",
        "rating": "4.6",
        "time": "20-25 min",
        "price": "₹",
        "location": "Dindigul",
        "description": "Fresh and juicy shawarmas packed with flavour.",
        "image": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?auto=format&fit=crop&w=1200&q=85",

        "foods": [
            {
                "id": "shawarma1",
                "name": "Chicken Shawarma",
                "price": 149,
                "image": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "shawarma2",
                "name": "Cheese Shawarma",
                "price": 179,
                "image": "https://images.unsplash.com/photo-1561651823-34feb02250e4?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "shawarma3",
                "name": "Peri Peri Shawarma",
                "price": 189,
                "image": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "shawarma4",
                "name": "Plate Shawarma",
                "price": 249,
                "image": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "shawarma5",
                "name": "Chicken Roll",
                "price": 159,
                "image": "https://images.unsplash.com/photo-1561651823-34feb02250e4?auto=format&fit=crop&w=900&q=85",
            },
            {
                "id": "shawarma6",
                "name": "Falafel Roll",
                "price": 139,
                "image": "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=900&q=85",
            },
        ],
    },
}


def restaurant_list(request):
    return render(
        request,
        "restaurants.html",
        {
            "restaurants": RESTAURANTS
        }
    )


def restaurant_detail(request, restaurant_id):

    restaurant = RESTAURANTS.get(restaurant_id)

    if not restaurant:
        return render(
            request,
            "restaurant_not_found.html",
            status=404
        )

    return render(
        request,
        "restaurant_detail.html",
        {
            "restaurant": restaurant,
            "restaurant_id": restaurant_id,
        }
    )
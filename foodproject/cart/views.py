from django.shortcuts import render, redirect


# ============================================================
# FOOD DATA
# ============================================================

FOODS = {

    # ---------------- A2B ----------------
    "a2b1": {
        "name": "Idli Sambar",
        "price": 80,
        "image": "https://images.unsplash.com/photo-1589302168068-964664d93dc0?w=800"
    },
    "a2b2": {
        "name": "Masala Dosa",
        "price": 120,
        "image": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?w=800"
    },
    "a2b3": {
        "name": "Paneer Dosa",
        "price": 160,
        "image": "https://images.unsplash.com/photo-1630383249896-424e482df921?w=800"
    },
    "a2b4": {
        "name": "Poori Masala",
        "price": 100,
        "image": "https://images.unsplash.com/photo-1626132647523-66f5bf380027?w=800"
    },
    "a2b5": {
        "name": "Veg Meals",
        "price": 150,
        "image": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=800"
    },
    "a2b6": {
        "name": "Paneer Rice",
        "price": 180,
        "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=800"
    },

    # ---------------- PIZZA ----------------
    "pizza1": {
        "name": "Classic Cheese Pizza",
        "price": 249,
        "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=800"
    },
    "pizza2": {
        "name": "Chicken Pizza",
        "price": 329,
        "image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800"
    },
    "pizza3": {
        "name": "Veg Loaded Pizza",
        "price": 279,
        "image": "https://images.unsplash.com/photo-1593560708920-61dd98c46a4e?w=800"
    },
    "pizza4": {
        "name": "Farmhouse Pizza",
        "price": 299,
        "image": "https://images.unsplash.com/photo-1579751626657-72bc17010498?w=800"
    },
    "pizza5": {
        "name": "Paneer Pizza",
        "price": 289,
        "image": "https://images.unsplash.com/photo-1579751626657-72bc17010498?w=800"
    },
    "pizza6": {
        "name": "Mexican Pizza",
        "price": 319,
        "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=800"
    },

    # ---------------- BIRYANI ----------------
    "biryani1": {
        "name": "Chicken Biryani",
        "price": 279,
        "image": "https://images.unsplash.com/photo-1563379091339-03246963d96c?w=800"
    },
    "biryani2": {
        "name": "Mutton Biryani",
        "price": 349,
        "image": "https://images.unsplash.com/photo-1633945274309-2c16c9682a8d?w=800"
    },
    "biryani3": {
        "name": "Egg Biryani",
        "price": 199,
        "image": "https://images.unsplash.com/photo-1633945274309-2c16c9682a8d?w=800"
    },
    "biryani4": {
        "name": "Chicken 65",
        "price": 220,
        "image": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=800"
    },
    "biryani5": {
        "name": "Mutton Sukka",
        "price": 299,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800"
    },
    "biryani6": {
        "name": "Grilled Chicken",
        "price": 299,
        "image": "https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=800"
    },

    # ---------------- BURGER ----------------
    "burger1": {
        "name": "Chicken Burger",
        "price": 199,
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800"
    },
    "burger2": {
        "name": "Classic Cheese Burger",
        "price": 179,
        "image": "https://images.unsplash.com/photo-1550547660-d9450f859349?w=800"
    },
    "burger3": {
        "name": "Double Chicken Burger",
        "price": 249,
        "image": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=800"
    },
    "burger4": {
        "name": "Veg Burger",
        "price": 149,
        "image": "https://images.unsplash.com/photo-1520072959219-c595dc870360?w=800"
    },
    "burger5": {
        "name": "Peri Peri Burger",
        "price": 219,
        "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=800"
    },
    "burger6": {
        "name": "Cheese Fries",
        "price": 139,
        "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=800"
    },

    # ---------------- CHINESE ----------------
    "noodles1": {
        "name": "Chicken Noodles",
        "price": 219,
        "image": "https://images.unsplash.com/photo-1552611052-33e04de081de?w=800"
    },
    "noodles2": {
        "name": "Veg Hakka Noodles",
        "price": 169,
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=800"
    },
    "rice1": {
        "name": "Chicken Fried Rice",
        "price": 229,
        "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=800"
    },
    "rice2": {
        "name": "Veg Fried Rice",
        "price": 179,
        "image": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=800"
    },
    "chinese1": {
        "name": "Chilli Chicken",
        "price": 249,
        "image": "https://images.unsplash.com/photo-1525755662778-989d0524087e?w=800"
    },
    "chinese2": {
        "name": "Gobi Manchurian",
        "price": 199,
        "image": "https://images.unsplash.com/photo-1625398407796-82650a8c135f?w=800"
    },

    # ---------------- SHAWARMA ----------------
    "shawarma1": {
        "name": "Chicken Shawarma",
        "price": 149,
        "image": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=800"
    },
    "shawarma2": {
        "name": "Cheese Shawarma",
        "price": 179,
        "image": "https://images.unsplash.com/photo-1544025162-d76694265947?w=800"
    },
    "shawarma3": {
        "name": "Peri Peri Shawarma",
        "price": 189,
        "image": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=800"
    },
    "shawarma4": {
        "name": "Plate Shawarma",
        "price": 249,
        "image": "https://images.unsplash.com/photo-1544025162-d76694265947?w=800"
    },
    "shawarma5": {
        "name": "Chicken Roll",
        "price": 159,
        "image": "https://images.unsplash.com/photo-1561651823-34feb02250e4?w=800"
    },
    "shawarma6": {
        "name": "Falafel Roll",
        "price": 139,
        "image": "https://images.unsplash.com/photo-1593001874117-c99c0f3c4e7b?w=800"
    },
}


# ============================================================
# ADD TO CART
# ============================================================

def add_to_cart(request, food_id):

    if food_id not in FOODS:
        return redirect("/restaurants/")

    cart = request.session.get("cart", {})

    if food_id in cart:
        cart[food_id]["quantity"] += 1
    else:
        food = FOODS[food_id]

        cart[food_id] = {
            "id": food_id,
            "name": food["name"],
            "price": food["price"],
            "image": food["image"],
            "quantity": 1,
        }

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("/cart/")


# ============================================================
# CART VIEW
# ============================================================

def cart_view(request):

    cart = request.session.get("cart", {})

    total = 0

    for item in cart.values():
        item["subtotal"] = item["price"] * item["quantity"]
        total += item["subtotal"]

    return render(
        request,
        "cart.html",
        {
            "cart": cart,
            "total": total,
        }
    )


# ============================================================
# INCREASE QUANTITY
# ============================================================

def increase_quantity(request, food_id):

    cart = request.session.get("cart", {})

    if food_id in cart:
        cart[food_id]["quantity"] += 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("/cart/")


# ============================================================
# DECREASE QUANTITY
# ============================================================

def decrease_quantity(request, food_id):

    cart = request.session.get("cart", {})

    if food_id in cart:

        if cart[food_id]["quantity"] > 1:
            cart[food_id]["quantity"] -= 1
        else:
            del cart[food_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("/cart/")


# ============================================================
# REMOVE ITEM
# ============================================================

def remove_from_cart(request, food_id):

    cart = request.session.get("cart", {})

    if food_id in cart:
        del cart[food_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("/cart/")


# ============================================================
# CLEAR CART
# ============================================================

def clear_cart(request):

    request.session["cart"] = {}
    request.session.modified = True

    return redirect("/cart/")


# ============================================================
# CHECKOUT
# ============================================================

def checkout(request):

    cart = request.session.get("cart", {})

    if not cart:
        return redirect("/cart/")

    total = 0

    for item in cart.values():
        item["subtotal"] = item["price"] * item["quantity"]
        total += item["subtotal"]

    # ---------------- POST ----------------

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        address = request.POST.get("address")
        payment = request.POST.get("payment")

        request.session["last_order"] = {
            "name": name,
            "phone": phone,
            "city": city,
            "address": address,
            "payment": payment,
            "items": list(cart.values()),
            "total": total,
        }

        # Clear cart after order
        request.session["cart"] = {}
        request.session.modified = True

        return redirect("/cart/order-success/")

    # ---------------- GET ----------------

    return render(
        request,
        "checkout.html",
        {
            "cart": cart,
            "total": total,
        }
    )


# ============================================================
# ORDER SUCCESS
# ============================================================

def order_success(request):

    order = request.session.get("last_order")

    if not order:
        return redirect("/restaurants/")

    return render(
        request,
        "order_success.html",
        {
            "order": order,
        }
    )
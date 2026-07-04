from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def restaurants(request):
    return render(request, 'restaurants.html')


def offers(request):
    return render(request, 'offers.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def cart(request):
    return render(request, 'cart.html')


def menu(request, name):

    foods = []

    if name == "a2b":
        foods = [
            {"name":"Idli","price":"₹50","image":"IMAGE_URL"},
            {"name":"Dosa","price":"₹80","image":"IMAGE_URL"},
            {"name":"Pongal","price":"₹90","image":"IMAGE_URL"},
            {"name":"Poori","price":"₹70","image":"IMAGE_URL"},
            {"name":"Meals","price":"₹120","image":"IMAGE_URL"},
            {"name":"Vada","price":"₹30","image":"IMAGE_URL"},
            {"name":"Chapati","price":"₹60","image":"IMAGE_URL"},
            {"name":"Parotta","price":"₹90","image":"IMAGE_URL"},
            {"name":"Mini Tiffin","price":"₹150","image":"IMAGE_URL"},
            {"name":"Filter Coffee","price":"₹40","image":"IMAGE_URL"},
        ]

    elif name == "pizza":
        foods = [
            {"name":"Cheese Pizza","price":"₹299","image":"IMAGE_URL"},
            {"name":"Veg Pizza","price":"₹249","image":"IMAGE_URL"},
            {"name":"Chicken Pizza","price":"₹399","image":"IMAGE_URL"},
            {"name":"Farm House Pizza","price":"₹499","image":"IMAGE_URL"},
            {"name":"Pepperoni Pizza","price":"₹599","image":"IMAGE_URL"},
            {"name":"Garlic Bread","price":"₹129","image":"IMAGE_URL"},
            {"name":"Pasta","price":"₹199","image":"IMAGE_URL"},
            {"name":"French Fries","price":"₹99","image":"IMAGE_URL"},
            {"name":"Burger","price":"₹149","image":"IMAGE_URL"},
            {"name":"Cold Coffee","price":"₹120","image":"IMAGE_URL"},
        ]

    elif name == "biryani":
        foods = [
            {"name":"Chicken Biryani","price":"₹249","image":"IMAGE_URL"},
            {"name":"Mutton Biryani","price":"₹349","image":"IMAGE_URL"},
            {"name":"Egg Biryani","price":"₹199","image":"IMAGE_URL"},
            {"name":"Fish Biryani","price":"₹299","image":"IMAGE_URL"},
            {"name":"Prawn Biryani","price":"₹399","image":"IMAGE_URL"},
            {"name":"Grill Chicken","price":"₹499","image":"IMAGE_URL"},
            {"name":"Tandoori Chicken","price":"₹450","image":"IMAGE_URL"},
            {"name":"Chicken 65","price":"₹180","image":"IMAGE_URL"},
            {"name":"Naan","price":"₹50","image":"IMAGE_URL"},
            {"name":"Falooda","price":"₹120","image":"IMAGE_URL"},
        ]

    elif name == "burger":
        foods = [
            {"name":"Cheese Burger","price":"₹149","image":"IMAGE_URL"},
            {"name":"Chicken Burger","price":"₹179","image":"IMAGE_URL"},
            {"name":"Double Patty Burger","price":"₹199","image":"IMAGE_URL"},
            {"name":"Veg Burger","price":"₹129","image":"IMAGE_URL"},
            {"name":"French Fries","price":"₹99","image":"IMAGE_URL"},
            {"name":"Peri Peri Fries","price":"₹129","image":"IMAGE_URL"},
            {"name":"Nuggets","price":"₹159","image":"IMAGE_URL"},
            {"name":"Hot Dog","price":"₹149","image":"IMAGE_URL"},
            {"name":"Sandwich","price":"₹129","image":"IMAGE_URL"},
            {"name":"Chocolate Shake","price":"₹140","image":"IMAGE_URL"},
        ]

    elif name == "chinese":
        foods = [
            {"name":"Veg Fried Rice","price":"₹180","image":"IMAGE_URL"},
            {"name":"Chicken Fried Rice","price":"₹220","image":"IMAGE_URL"},
            {"name":"Schezwan Rice","price":"₹210","image":"IMAGE_URL"},
            {"name":"Hakka Noodles","price":"₹190","image":"IMAGE_URL"},
            {"name":"Chicken Noodles","price":"₹220","image":"IMAGE_URL"},
            {"name":"Manchurian","price":"₹180","image":"IMAGE_URL"},
            {"name":"Spring Roll","price":"₹150","image":"IMAGE_URL"},
            {"name":"Momos","price":"₹140","image":"IMAGE_URL"},
            {"name":"Dragon Chicken","price":"₹260","image":"IMAGE_URL"},
            {"name":"Hot & Sour Soup","price":"₹120","image":"IMAGE_URL"},
        ]

    elif name == "shawarma":
        foods = [
            {"name":"Chicken Shawarma","price":"₹120","image":"IMAGE_URL"},
            {"name":"Arabic Shawarma","price":"₹150","image":"IMAGE_URL"},
            {"name":"Mexican Shawarma","price":"₹170","image":"IMAGE_URL"},
            {"name":"Plate Shawarma","price":"₹220","image":"IMAGE_URL"},
            {"name":"Cheese Shawarma","price":"₹180","image":"IMAGE_URL"},
            {"name":"Zinger Shawarma","price":"₹190","image":"IMAGE_URL"},
            {"name":"Chicken Roll","price":"₹130","image":"IMAGE_URL"},
            {"name":"Grill Chicken","price":"₹350","image":"IMAGE_URL"},
            {"name":"Garlic Mayo","price":"₹50","image":"IMAGE_URL"},
            {"name":"Fresh Juice","price":"₹90","image":"IMAGE_URL"},
        ]

    elif name == "pizzahut":
        foods = [
            {"name":"Margherita Pizza","price":"₹299","image":"IMAGE_URL"},
            {"name":"Veg Supreme","price":"₹399","image":"IMAGE_URL"},
            {"name":"Chicken Supreme","price":"₹499","image":"IMAGE_URL"},
            {"name":"Paneer Pizza","price":"₹349","image":"IMAGE_URL"},
            {"name":"Tandoori Pizza","price":"₹449","image":"IMAGE_URL"},
            {"name":"Garlic Bread","price":"₹129","image":"IMAGE_URL"},
            {"name":"Pasta Alfredo","price":"₹199","image":"IMAGE_URL"},
            {"name":"Choco Lava Cake","price":"₹99","image":"IMAGE_URL"},
            {"name":"Pepsi","price":"₹60","image":"IMAGE_URL"},
            {"name":"Brownie","price":"₹120","image":"IMAGE_URL"},
        ]

    elif name == "arabian":
        foods = [
            {"name":"Al Faham","price":"₹350","image":"IMAGE_URL"},
            {"name":"Mandi","price":"₹450","image":"IMAGE_URL"},
            {"name":"Kuzhi Mandi","price":"₹550","image":"IMAGE_URL"},
            {"name":"Chicken Kabsa","price":"₹420","image":"IMAGE_URL"},
            {"name":"Grill Chicken","price":"₹380","image":"IMAGE_URL"},
            {"name":"Chicken Kebab","price":"₹250","image":"IMAGE_URL"},
            {"name":"Hummus","price":"₹120","image":"IMAGE_URL"},
            {"name":"Kuboos","price":"₹20","image":"IMAGE_URL"},
            {"name":"Kunafa","price":"₹180","image":"IMAGE_URL"},
            {"name":"Arabic Tea","price":"₹50","image":"IMAGE_URL"},
        ]

    return render(
        request,
        'menu.html',
        {
            'foods': foods,
            'restaurant_name': name
        }
    )
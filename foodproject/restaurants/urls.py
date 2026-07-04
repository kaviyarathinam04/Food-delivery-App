from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('restaurants/', views.restaurants, name='restaurants'),

    path('offers/', views.offers, name='offers'),

    path('register/', views.register, name='register'),

    path('login/', views.login, name='login'),

    path('cart/', views.cart, name='cart'),

    path('menu/<str:name>/', views.menu, name='menu'),

]
from django.db import models
from django.conf import settings
from menu.models import FoodItem


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )
    food_item = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    @property
    def item_total(self):
        return self.food_item.price * self.quantity

    def __str__(self):
        return f"{self.food_item.name} x {self.quantity}"
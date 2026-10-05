from django.db import models
from restaurants.models import Restaurant


class FoodItem(models.Model):

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="foods"
    )

    name = models.CharField(max_length=150)

    category = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    image = models.URLField(blank=True)

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
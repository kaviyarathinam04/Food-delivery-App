from django.db import models


class Restaurant(models.Model):

    name = models.CharField(max_length=150)

    category = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    image = models.URLField(blank=True)

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=4.5
    )

    delivery_time = models.CharField(
        max_length=50,
        default="30-40 min"
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
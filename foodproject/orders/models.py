from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):

    STATUS_CHOICES = [
        ("PLACED", "Placed"),
        ("CONFIRMED", "Confirmed"),
        ("PREPARING", "Preparing"),
        ("OUT", "Out for Delivery"),
        ("DELIVERED", "Delivered"),
    ]

    PAYMENT_CHOICES = [
        ("COD", "Cash on Delivery"),
        ("UPI", "UPI"),
        ("CARD", "Card"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    customer_name = models.CharField(
        max_length=150
    )

    phone = models.CharField(
        max_length=20
    )

    address = models.TextField()

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default="COD"
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="PLACED"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order #{self.id}"
from typing import Iterable
from django.db import models
from django.contrib.auth import get_user_model

from shop.models import Product

# Create your models here.

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, related_name="cart_items"
    )
    quantity = models.IntegerField(default=1, null=True, verbose_name="Quantity")
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Total_price",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def save(self, *args, **kwargs):
        if self.pk or not self.total_price:
            self.total_price = self.quantity * float(self.product.current_price)
        return super().save(*args, **kwargs)

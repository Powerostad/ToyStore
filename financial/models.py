from typing import Iterable
from django.db import models
from django.contrib.auth import get_user_model
from cart.models import Cart

# Create your models here.
User = get_user_model()


class Payment(models.Model):
    PAYMENT_CHOICE = (
        ("a", "Accept"),
        ("r", "Reject"),
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    accept = models.CharField(max_length=1, choices=PAYMENT_CHOICE, default="A")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.amount:
            self.amount = sum(item.total_price for item in self.cart.cart_item.all())
        if not self.amount:
            self.user = self.cart.user
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cart.user.username} . {self.amount} . {self.updated_at}"

    class Meta:
        ordering = ("-updated_at",)

from typing import Iterable
from django.db import models
from django.contrib.auth import get_user_model
from cart.models import Cart

# Create your models here.
User = get_user_model()


class Payment(models.Model):
    PAYMENT_CHOICE = (
        ("o", "Online"),
        ("i", "In person"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_method = models.CharField(max_length=1, choices=PAYMENT_CHOICE, default="o")
    paid_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.amount:
            self.amount = sum(item.total_price for item in self.cart.cart_item.all())
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user.username}.{self.amount}.{self.paid_at}"

    class Meta:
        ordering = ("-paid_at",)

from rest_framework import serializers
from .models import Cart, CartItem


class CartSerializer(serializers.ModelField):
    class Meta:
        model = Cart
        fields = (
            "user",
            "created_at",
            "updated_at",
        )


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            "cart",
            "product",
            "quantity",
            "total_price",
        )

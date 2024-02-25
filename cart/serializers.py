from rest_framework import serializers
from .models import Cart, CartItem
from shop.serializers import ProductSerializer
from shop.models import Product


class CartSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = Cart
        fields = (
            "user",
            "created_at",
            "updated_at",
        )


class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True
    )
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = (
            "cart",
            "product",
            "product_id",
            "quantity",
            "total_price",
        )
        extra_kwargs = {
            "total_price": {"read_only": True},
        }

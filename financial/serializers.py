from rest_framework import serializers
from .models import Payment
from cart.serializers import CartSerializer


class PaymentSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=False, required=False)

    class Meta:
        model = Payment
        fields = (
            "cart",
            "amount",
            "is_paid",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "amount": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

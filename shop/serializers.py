from rest_framework import serializers
from .models import ShopCategory, ShopComment, Price, Product, ShopGallery


class ShopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCategory
        fields = (
            "name",
            "slug",
        )


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            "price",
            "created",
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "category",
            "thumbnail",
            "stock",
            "available",
            "created_at",
            "updated_at",
        )


class ShopGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopGallery
        fields = (
            "product",
            "image",
            "video",
        )


class ShopCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopComment
        fields = (
            "product",
            "user",
            "content",
            "created_on",
            "active",
        )

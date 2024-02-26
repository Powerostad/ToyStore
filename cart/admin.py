from django.contrib import admin
from .models import Cart, CartItem


# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id",)
    list_filter = (
        "user",
        "created_at",
        "updated_at",
    )
    search_fields = ("user",)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cart",
        "product",
        "quantity",
        "total_price",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "cart",
        "product",
    )
    list_filter = (
        "cart",
        "product",
        "quantity",
        "total_price",
        "created_at",
        "updated_at",
    )

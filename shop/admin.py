from django.contrib import admin
from .models import ShopCategory, ShopComment, ShopGallery, Product, Price

# Register your models here.


@admin.register(ShopCategory)
class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )
    list_display_links = ("id",)
    search_fields = ("name", "slug")


@admin.register(ShopComment)
class ShopCommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content",
        "product",
        "user",
        "created_on",
        "active",
    )
    list_display_links = ("id", "content")
    list_editable = ("active",)
    list_filter = (
        "product",
        "user",
        "created_on",
        "active",
    )
    search_fields = ("product", "content")


@admin.register(ShopGallery)
class ShopGalleryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "media",
        "active",
    )
    list_display_links = ("id", "product")
    list_editable = ("active",)
    list_filter = ("product", "active")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "slug",
        "current_price_display",
        "get_category",
        "stock",
        "available",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("current_price_display",)
    list_display_links = ("id", "name")
    list_filter = (
        "price",
        "category",
        "stock",
        "available",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "description",
    )

    def get_category(self, obj):
        return ", ".join([c.name for c in obj.category.all()])

    def current_price_display(self, obj):
        return obj.current_price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "price",
        "created",
    )
    list_display_links = ("id", "price")
    list_filter = ("price",)

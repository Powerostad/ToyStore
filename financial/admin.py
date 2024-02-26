from django.contrib import admin
from .models import Payment

# Register your models here.


@admin.register(Payment)
class PaymnetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cart",
        "amount",
        "is_paid",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "cart")
    list_filter = (
        "cart",
        "is_paid",
        "created_at",
        "updated_at",
    )
    list_editable = ("is_paid",)

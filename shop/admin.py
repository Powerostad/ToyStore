from django.contrib import admin
from .models import ShopCategory, ShopComment, ShopGallery, Product, Price

# Register your models here.

admin.site.register(ShopCategory)
admin.site.register(ShopComment)
admin.site.register(ShopGallery)
admin.site.register(Product)
admin.site.register(Price)

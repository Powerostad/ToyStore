from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class ShopCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(
        max_length=250,
        populate_from="name",
        editable=True,
        always_update=True,
    )

    def __str__(self) -> str:
        return self.name.title


class Price(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self) -> str:
        return self.price


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="product_name")
    description = models.TextField(verbose_name="description")
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name="product")
    category = models.ManyToManyField(ShopCategory, related_name="products")
    thumbnail = models.ImageField(
        default="no-image.jpg", null=True, verbose_name="product_thumbnail"
    )
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="product_created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="product_updated")

    def __str__(self) -> str:
        return self.name


class ShopGallery(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="shop_gallery"
    )
    image = models.ImageField(null=True)
    video = models.FileField(null=True)

    def __str__(self) -> str:
        return f"Gallery of {self.product.pk}.{self.product.name}"


class ShopComment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_comments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="product_comments"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        if len(self.content) > 100:
            return self.content[:100]
        return self.content

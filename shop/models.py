from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

User = get_user_model()


# Create your models here.
class ShopCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(
        max_length=250,
        populate_from="name",
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="product_name")
    description = models.TextField(verbose_name="description")
    slug = AutoSlugField(
        max_length=250,
        populate_from="name",
        unique_for_date="created_at",
        null=True,
        blank=True,
        default=None,
    )

    @property
    def current_price(self):
        return self.price.values_list("price", flat=True).first()

    category = models.ManyToManyField(ShopCategory, related_name="products")
    thumbnail = models.ImageField(
        default="no-image.jpg", null=True, blank=True, verbose_name="product_thumbnail"
    )
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="product_created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="product_updated")

    def __str__(self):
        return self.name


class Price(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.price)


class ShopGallery(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="shop_gallery"
    )
    media = RichTextUploadingField("image_or_video", null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"Gallery of {self.product.pk}.{self.product.name}"


class ShopComment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_comments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="product_comments"
    )
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        if len(self.content) > 100:
            return self.content[:100]
        return self.content

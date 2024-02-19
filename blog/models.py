from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from autoslug import AutoSlugField

# Create your models here.
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(
        max_length=250,
        populate_from="name",
        editable=True,
        always_update=True,
    )

    def __str__(self) -> str:
        return self.name.title


class Post(models.Model):
    STATUS_CHOCIE = [
        ("D", "Draft"),
        ("P", "Published"),
    ]
    title = models.CharField(max_length=100, verbose_name="Title")
    body = models.TextField(verbose_name="Body")
    slug = AutoSlugField(
        max_length=250,
        populate_from="title",
        editable=True,
        always_update=True,
        unique_for_date="published",
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ManyToManyField(Category, related_name="posts")
    thumbnail = models.ImageField(verbose_name="Thumbnail")
    published = models.DateTimeField(default=timezone.now(), verbose_name="Published")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated")
    status = models.CharField(
        choices=STATUS_CHOCIE, max_length=1, verbose_name="Status"
    )

    class Meta:
        ordering = ("-published",)

    def __str__(self) -> str:
        return self.title


class Gallery(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(null=True)
    video = models.FileField(null=True)

    def __str__(self) -> str:
        return f"Gallery of {self.post.pk}.{self.post.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        if len(self.content) > 100:
            return self.content[:100]
        return self.content

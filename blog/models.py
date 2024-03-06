from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# from django.utils import timezone
from autoslug import AutoSlugField

# from .tasks import check_published_posts

# Create your models here.
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(
        max_length=250,
        populate_from="name",
        unique=True,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOCIE = (
        ("D", "Draft"),
        ("P", "Published"),
    )
    title = models.CharField(max_length=100, verbose_name="Title")
    body = models.TextField(verbose_name="Body")
    slug = AutoSlugField(
        max_length=250,
        populate_from="title",
        unique=True,
        null=True,
        blank=True,
        default=None,
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ManyToManyField(Category, related_name="posts")
    thumbnail = models.ImageField(
        default="no-image.jpg", null=True, blank=True, verbose_name="Thumbnail"
    )
    # published = models.DateTimeField(default=timezone.now(), verbose_name="Published")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated")
    status = models.CharField(
        choices=STATUS_CHOCIE, max_length=1, verbose_name="Status"
    )

    class Meta:
        ordering = ("-created_at",)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     check_published_posts.delay()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="gallery")
    media = RichTextUploadingField("image_or_video", null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"Gallery of {self.post.pk}.{self.post.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        if len(self.content) > 100:
            return self.content[:100]
        return self.content

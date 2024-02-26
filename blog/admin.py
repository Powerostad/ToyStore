from django.contrib import admin
from .models import Category, Post, Comment, Gallery

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )
    list_display_links = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "body",
        "slug",
        "author",
        "get_category",
        "created_at",
        "updated_at",
        "status",
    )
    list_editable = ("status",)
    list_display_links = ("title",)
    list_filter = (
        "author",
        "updated_at",
        "created_at",
        "status",
    )
    search_fields = ("title", "body", "author")

    def get_category(self):
        return "\n".join([p.name for p in self.category.all()])


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content",
        "post",
        "user",
        "created_on",
        "active",
    )
    list_display_links = ("content",)
    list_filter = ("post", "user", "active", "created_on")
    list_editable = ("active",)
    search_fields = ("content", "post", "user")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "media",
        "post",
        "active",
    )
    list_display_links = ("media",)
    list_filter = (
        "post",
        "active",
    )
    search_fields = ("post",)

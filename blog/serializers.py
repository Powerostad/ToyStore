from rest_framework import serializers
from .models import Category, Post, Comment, Gallery


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "slug",
        )


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    post = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Comment
        fields = (
            "post",
            "user",
            "content",
            "created_on",
        )
        extra_kwargs = {
            "user": {"read_only": True},
            "post": {"read_only": True},
        }


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="name", many=True, read_only=True
    )
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    comments = CommentSerializer(many=True, read_only=False)

    class Meta:
        model = Post
        fields = (
            "title",
            "body",
            "slug",
            "author",
            "comments",
            "category",
            "thumbnail",
            "created_at",
            "updated_at",
            "status",
        )


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = (
            "post",
            "image",
            "video",
        )

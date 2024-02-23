from rest_framework import serializers
from .models import Category, Post, Comment, Gallery


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "slug",
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "body",
            "slug",
            "author",
            "category",
            "thumbnail",
            "created_at",
            "updated_at",
            "status",
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "post",
            "user",
            "content",
            "created_on",
            "active",
        )


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = (
            "post",
            "image",
            "video",
        )

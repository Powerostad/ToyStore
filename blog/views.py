from rest_framework import viewsets
from .models import Category, Post, Comment, Gallery
from .serializers import (
    CategorySerializer,
    PostSerializer,
    GallerySerializer,
    CommentSerializer,
)

# Create your views here.


class CategoryList(viewsets.ReadOnlyModelViewSet):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "slug"


class PostList(viewsets.ReadOnlyModelViewSet):
    model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "slug"

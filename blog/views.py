from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
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
    lookup_url_kwarg = "slug"

    search_fields = ["^title", "=author__username"]

    filterset_fields = {
        "title": ["icontains", "startswith"],
        "author__username": [
            "icontains",
        ],
        "status": ["exact"],
        "created_at": ["date__exact"],
    }


class CommentList(viewsets.ReadOnlyModelViewSet):
    model = Comment
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(active=True)

    search_fields = ["^content", "=user__username"]

    filterset_fields = {
        "post__title": ["icontains", "startswith"],
        "user__username": [
            "icontains",
        ],
        "created_on": ["date__exact"],
    }


class PostCommentCreate(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post = self.kwargs["slug_slug"]
        return Comment.objects.filter(post__slug=post, active=True)

    def create(self, request, *args, **kwargs):

        post_slug = kwargs["slug_slug"]
        post = Post.objects.get(slug=post_slug)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user, post=post)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryList, PostList, CommentList, PostCommentCreate
from rest_framework_nested import routers

router = DefaultRouter()
router.register(r"blog-genres", CategoryList)
router.register(r"blog-posts", PostList)
router.register(r"blog-comments", CommentList)
nested_post = routers.NestedDefaultRouter(router, r"blog-posts", lookup="slug")
nested_post.register(r"comments", PostCommentCreate, basename="post_comments")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(nested_post.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryList, PostList

router = DefaultRouter()

router.register(r"blog-genres", CategoryList)
router.register(r"blog-posts", PostList)

urlpatterns = [
    path("", include(router.urls)),
]

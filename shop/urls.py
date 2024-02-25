from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShopCategoryList, ProductList, ShopCommentsList, ShopCommentCreate
from rest_framework_nested import routers

router = DefaultRouter()
router.register(r"shopcategory", ShopCategoryList, basename="shop-categories")
router.register(r"shopproducts", ProductList, basename="shop-products")
router.register(r"shopcomments", ShopCommentsList, basename="shop-comments")

product_comment = routers.NestedDefaultRouter(router, r"shopproducts", lookup="product")
product_comment.register(r"comments", ShopCommentCreate, basename="product_comment")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(product_comment.urls)),
]

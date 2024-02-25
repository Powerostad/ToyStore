from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartItemViewSet, AddToCartView

router = DefaultRouter()
router.register(r"cartitems", CartItemViewSet, basename="add-item")

urlpatterns = [
    path("cartitems/<int:pk>/", CartItemViewSet.as_view()),
    path("additem/", AddToCartView.as_view()),
]

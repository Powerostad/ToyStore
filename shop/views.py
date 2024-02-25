from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from .models import ShopCategory, Price, Product, ShopGallery, ShopComment
from .serializers import (
    ShopCategorySerializer,
    PriceSerializer,
    ProductSerializer,
    ShopCommentSerializer,
    ShopGallerySerializer,
)


# Create your views here.


class ShopCategoryList(viewsets.ReadOnlyModelViewSet):
    model = ShopCategory
    serializer_class = ShopCategorySerializer
    queryset = ShopCategory.objects.all()
    lookup_field = "slug"


class ProductList(viewsets.ReadOnlyModelViewSet):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    search_fields = ["^name", "=category"]

    filterset_fields = {
        "name": ["icontains", "startswith"],
        "description": ["icontains"],
        "available": ["exact"],
        "price": ["gte", "lte"],
        "updated_at": ["date__exact"],
    }


class ShopCommentsList(viewsets.ReadOnlyModelViewSet):
    model = ShopComment
    serializer_class = ShopCommentSerializer

    def get_queryset(self):
        queryset = ShopComment.objects.all()

        if self.request.user.is_staff:
            return queryset
        else:
            return queryset.filter(active=True)


class ShopCommentCreate(viewsets.ModelViewSet):
    serializer_class = ShopCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        product = self.kwargs["product_pk"]
        if self.request.user.is_staff:
            return ShopComment.objects.filter(product_id=product)
        else:
            return ShopComment.objects.filter(product_id=product, active=True)

    def create(self, request, *args, **kwargs):

        product_pk = kwargs["product_pk"]
        product = Product.objects.get(pk=product_pk)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user, product=product)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

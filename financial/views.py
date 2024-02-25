from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer
from cart.models import Cart

# Create your views here.


class PaymentList(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "put"]

    def get_queryset(self):
        user = self.request.user
        query = Payment.objects.all()
        if user.is_staff:
            return query
        else:
            return query.filter(cart__user=user)

    def update(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            payment = self.get_object()
            serializer = self.serializer_class(payment, data=request.data)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        return Response("You are not Admin", status=status.HTTP_403_FORBIDDEN)

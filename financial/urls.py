from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentList
from rest_framework_nested import routers


router = DefaultRouter()
router.register(r"payment", PaymentList, basename="payment")

# update_payment = routers.NestedDefaultRouter()
urlpatterns = [
    path("", include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CarViewSet, ColorViewSet, MaterialViewSet,
    CarImageViewSet, FAQViewSet, ContactMessageViewSet
)

router = DefaultRouter()
router.register(r"cars", CarViewSet)
router.register(r"colors", ColorViewSet)
router.register(r"materials", MaterialViewSet)
router.register(r"images", CarImageViewSet)
router.register(r"faq", FAQViewSet)
router.register(r"contacts", ContactMessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

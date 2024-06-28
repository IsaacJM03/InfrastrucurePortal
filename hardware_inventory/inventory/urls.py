from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, HardwareItemViewSet

router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
]
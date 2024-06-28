"""
URL configuration for hardware_inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from users.views import UserRegistrationAPIView, ObtainAuthToken
from inventory.views import HardwareItemViewSet
from devices.views import DeviceViewSet, NetworkPortViewSet,GNS3ProjectAPIView


router = DefaultRouter()
# router.register(r'users',UserViewSet)
router.register(r'hardware-items', HardwareItemViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'network-ports', NetworkPortViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('api/login/', ObtainAuthToken.as_view(), name='user-login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # testing with gns3
    path('gns3/projects/', GNS3ProjectAPIView.as_view(), name='gns3-projects'),
]

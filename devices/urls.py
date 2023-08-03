from django.urls import path, include
from rest_framework import routers
from .api import DeviceViewSet
from .api import DeviceUpdateAPIView
from . import views

router = routers.DefaultRouter()
router.register(r'api/devices', DeviceViewSet)

urlpatterns = [
    path('list/', views.device_list, name='device_list'),
    path('add/', views.add_device, name='add_device'),
    path('api/devices/<int:device_id>/update/', DeviceUpdateAPIView.as_view(), name='api_device_update'),
    path('api/', include(router.urls)),
]
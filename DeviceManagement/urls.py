from django.contrib import admin
from django.urls import path, include
from devices.views import device_list  # Import the device_list view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('devices/', include('devices.urls')),
    path('', device_list, name='root_device_list'),  # Add this line for the root URL
]

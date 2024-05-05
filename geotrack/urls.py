from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path ('admin/', admin.site.urls),
    path ('', include('device.urls'), name= 'device_urls')
]
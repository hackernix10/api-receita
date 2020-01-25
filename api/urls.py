from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from core import urls as core_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
]

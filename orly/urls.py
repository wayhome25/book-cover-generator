from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cover/', include('cover.urls', namespace='cover')),
    path('', lambda r: redirect('cover:index')),
]

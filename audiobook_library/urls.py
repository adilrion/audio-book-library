# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('audiobooks.urls')),
    path('admin/', admin.site.urls),
]

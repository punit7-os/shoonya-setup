from django.contrib import admin
from . import views

from django.urls import include, path

urlpatterns = [
    path("", views.index),
    path("tentothree/", include("tentothree.urls")),
    path("admin/", admin.site.urls),
]
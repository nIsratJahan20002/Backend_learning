from django.contrib import admin
from django.urls import path, include


MY_CUSTOM_URLS = [
    path("", include("blogs.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lalalala/", include(MY_CUSTOM_URLS)),
]

# fixture

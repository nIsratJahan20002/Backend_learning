from django.urls import path
from . import views

urlpatterns = [
    path("library-1-to-1/", views.library, name="library"),
]
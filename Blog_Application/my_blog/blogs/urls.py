from django.urls import path
from . import views

urlpatterns = [
  path("blog/", views.index,name="blog.list"),
  path("one-to-one/",views.reldemo,name="reldemo"),
]
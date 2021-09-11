from django.urls import path

from . import views

urlpatterns = [path("test/", views.index, name="index"),
               path("test2/", views.index2, name="index2"),
               path("", views.index3, name="index3")]

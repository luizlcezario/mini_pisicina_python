from django.urls import path

from . import views

urlpatterns = [
    path('', views.Ex00_movies().get, name="index")
]

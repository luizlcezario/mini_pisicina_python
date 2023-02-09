from django.urls import path

from . import views

app_name = "ex02"
urlpatterns = [
    path('', views.index, name="index")
]

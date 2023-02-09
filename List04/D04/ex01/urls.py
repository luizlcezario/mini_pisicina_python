# djangotemplates/example/urls.py

from django.urls import path

from ex01 import views


urlpatterns = [
    path('django', views.Djangoview.as_view(), name='django'),  # Add this URL pattern
    path('display', views.Displayview.as_view(), name='display'),  # Add this URL pattern
    path('templates', views.Templatesview.as_view(), name='templates'),  # Add this URL pattern
]  
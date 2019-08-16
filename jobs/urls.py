from django.urls import path

from .import views

urlpatterns = [
    path('jquery1', views.jquery1 , name='jquery1'),
    path('jquery2', views.jquery2 , name='jquery2'),

    ]
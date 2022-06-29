from . import views #el punto significa que desde el mismo directorio buscamos el archivo
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
]

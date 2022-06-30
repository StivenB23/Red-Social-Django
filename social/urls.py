from . import views #el punto significa que desde el mismo directorio buscamos el archivo
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView #utilizar vista de django predifinida

urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register , name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('post/', views.post, name='post' )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

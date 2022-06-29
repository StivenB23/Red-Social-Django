from django.contrib import admin
from .models import Post, Profile
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
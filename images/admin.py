from django.contrib import admin
from .models import Image, Comment

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']


@admin.register(Comment)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'body','created']
    list_filter = ['created']
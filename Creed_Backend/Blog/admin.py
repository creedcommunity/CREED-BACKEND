from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['category', 'author', 'tital']
    search_fields = ['category']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'name', 'post', 'created_at']
    search_fields = ['name']


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)

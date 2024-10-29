from django.contrib import admin
from .models import *


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'image', 'born_date', 'created_at', 'updated_at')
    list_filter = ('born_date',)
    search_fields = ('last_name',)
    ordering = ('last_name',)


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'content', 'published_date', 'created_at', 'updated_at')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'author')
    ordering = ('title',)

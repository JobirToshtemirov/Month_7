from django.contrib import admin
from .models import *


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'born_date')
    list_filter = ('born_date',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'isbn', 'price')
    list_filter = ('author', 'price')
    search_fields = ('title', 'author__name')
    ordering = ('title',)

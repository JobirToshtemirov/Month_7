from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/detail/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('authors/update/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('authors/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author-delete'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListCreateView.as_view(), name='blog-list-create'),
    # path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog-delete'),
    path('users/', UserListView.as_view(), name='users-list'),
    path('users/create', UserCreateView.as_view(), name='user-create'),
    path('users/detail/<int:pk>/', UserDetailView.as_view(), name='users-detail'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='users-update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='users-delete'),
]

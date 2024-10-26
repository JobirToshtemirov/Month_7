from django.shortcuts import render
from .models import BookModel, AuthorModel
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BookListView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination


class BookDetailView(generics.RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDeleteView(generics.DestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorListView(generics.ListAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = StandardResultsSetPagination


class AuthorDetailView(generics.RetrieveAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateView(generics.UpdateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorDeleteView(generics.DestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

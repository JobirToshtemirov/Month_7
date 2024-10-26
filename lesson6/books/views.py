from django.shortcuts import render
from .models import BookModel
from .serializers import BookSerializer

from rest_framework import generics


class BookListView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

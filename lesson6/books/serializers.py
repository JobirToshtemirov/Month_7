from rest_framework import serializers
from .models import BookModel, AuthorModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('id', 'name', 'image', 'born_date')


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = BookModel
        fields = ('id', 'title', 'subtitle', 'author', 'isbn', 'price')

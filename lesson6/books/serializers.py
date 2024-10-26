from rest_framework import serializers
from .models import BookModel, AuthorModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('id', 'name', 'image', 'born_date')


class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(queryset=AuthorModel.objects.all(), source='author')

    class Meta:
        model = BookModel
        fields = ('id', 'title', 'subtitle', 'author_id', 'isbn', 'price')

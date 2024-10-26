from rest_framework import serializers
from .models import BookModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('title', 'subtitle', 'author', 'isbn', 'price',)

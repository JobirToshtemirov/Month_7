from rest_framework import serializers
from .models import BlogModel, UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'image', 'born_date', 'created_at', 'updated_at')


class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = BlogModel
        fields = ('id', 'title', 'author', 'content', 'published_date', 'created_at', 'updated_at')

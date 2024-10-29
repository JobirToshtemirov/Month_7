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
        extra_kwargs = {'author': {'read_only': True}}

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, created = UserModel.objects.get_or_create(**author_data)
        blog = BlogModel.objects.create(author=author, **validated_data)
        return blog


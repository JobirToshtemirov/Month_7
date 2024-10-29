# Create your models here.
from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='users/')
    born_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='blogs')
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def __str__(self):
        return self.title

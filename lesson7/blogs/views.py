from .models import BlogModel, UserModel
from .serializers import BlogSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    pagination_class = StandardResultsSetPagination


class BlogDetailView(generics.RetrieveAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


class BlogUpdateView(generics.UpdateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BlogDeleteView(generics.DestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserListView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination


class UserCreateView(generics.CreateAPIView):
    queryset =  UserModel.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserDeleteView(generics.DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from . models import UserModel
from .serializers import SignUpSerializer


class CreateUserModelView(CreateAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = SignUpSerializer

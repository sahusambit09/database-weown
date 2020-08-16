from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserInfoSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import UserInfo


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserInfoViewset(viewsets.ModelViewSet):
    print("this is working")
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

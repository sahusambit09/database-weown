from rest_framework import serializers
from .models import UserInfo
from django.contrib.auth.models import User


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'url', 'dob', 'user', 'postal_code', 'country', 'nationality']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

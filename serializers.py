#coding=utf-8

from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'groups', 'user_permissions',
                  'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')
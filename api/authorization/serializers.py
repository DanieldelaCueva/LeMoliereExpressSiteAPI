from rest_framework import serializers
from .models import UserData
from django.contrib.auth.models import User
from .models import UserData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['age_class', 'group']

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password']


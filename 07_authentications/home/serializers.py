from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length = 100)
    first_name = serializers.CharField(max_length = 100)
    last_name = serializers.CharField(max_length = 100)

    def validate_username(self, username):
        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError('username already exist')
        return username
    
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length = 100)
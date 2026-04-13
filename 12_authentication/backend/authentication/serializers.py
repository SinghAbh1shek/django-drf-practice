from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length = 100)
    last_name = serializers.CharField(max_length = 100)
    email = serializers.EmailField(max_length = 100)
    username = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length = 100, write_only=True)

    def validate_username(self, data):
        user = User.objects.filter(username = data)
        if user.exists():
            raise serializers.ValidationError('username already exist')
        return data
    
    def validate_email(self, data):
        user = User.objects.filter(email = data)
        if user.exists():
            raise serializers.ValidationError('email already exist')
        return data
    
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
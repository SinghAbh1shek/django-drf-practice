from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length = 100)
    email = serializers.EmailField(max_length = 100)
    password = serializers.CharField(max_length = 100, write_only=True)

    def validate_email(self, data):
        user = User.objects.filter(email=data)
        if user.exists():
            raise serializers.ValidationError('email already exist')
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 100)
    password = serializers.CharField(max_length = 100, write_only=True)


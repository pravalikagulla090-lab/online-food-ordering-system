from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # [cite: 3]

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'password', 'role'] # [cite: 3]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'], # [cite: 4]
            phone=validated_data.get('phone', ''), # [cite: 4]
            role=validated_data.get('role', 'customer'), # [cite: 4]
            password=validated_data['password'] # [cite: 4]
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'role'] # [cite: 4]
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Test


# ---------------------------------------------------
# Test Serializer
# ---------------------------------------------------
# Handles CRUD serialization for Test model.
# - Converts model instances <-> JSON
# - Owner is read-only (auto-assigned in ViewSet)
# ---------------------------------------------------

class TestSerializer(serializers.ModelSerializer):
    # Show owner's string representation (usually username)
    # Prevent client from manually setting owner
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Test
        fields = '__all__'
        read_only_fields = ['owner']


# ---------------------------------------------------
# Register Serializer
# ---------------------------------------------------
# Handles user registration.
# - Validates unique username and email
# - Hashes password using create_user()
# - Password is write_only (never returned in response)
# ---------------------------------------------------

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # Ensure username is unique
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    # Ensure email is unique
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    # Create user with hashed password
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )


# ---------------------------------------------------
# Login Serializer
# ---------------------------------------------------
# Used only for validating login input.
# Does NOT create user.
# Only validates incoming credentials format.
# ---------------------------------------------------

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
# serializers.py
###################### custom JWT serializer to add extra claims ######################
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 🔥 Custom claims
        token['username'] = user.username
        token['is_staff'] = user.is_staff
        token['email'] = user.email
        token['groups'] = list(user.groups.values_list('name', flat=True))
        token["token_version"] = user.profile.token_version
        return token
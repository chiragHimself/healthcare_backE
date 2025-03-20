from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import Patient

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom JWT authentication using email instead of username"""
    
    username_field = User.EMAIL_FIELD  # Use email instead of username
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email  # Add email to the token payload
        return token



class UserSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""
    
    password = serializers.CharField(write_only=True, required=True)  # Ensure password is securely stored
    name = serializers.CharField(source='first_name', required=True)  # Accept 'name' instead of 'first_name'

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'name']

    def create(self, validated_data):
        """Override create method to hash password properly"""
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'user', 'name', 'age', 'gender', 'contact', 'address']  # Explicit fields
        extra_kwargs = {'user': {'read_only': True}}  

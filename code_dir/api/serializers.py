from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser, Patient


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "password", "role"]
        extra_kwargs = {
            "password": {"write_only": True},
            "role": {"read_only": True},
        }

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "A user with that username already exists."
            )
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            role="patient",
        )
        return user


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for the Patient model."""

    class Meta:
        model = Patient
        fields = ["id", "date_of_birth", "diagnoses", "created_at"]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom serializer for JWT token obtainment."""

    @classmethod
    def get_token(cls, user):
        """Add custom claims to the token."""
        token = super().get_token(user)
        token["username"] = user.username
        token["role"] = user.role
        return token

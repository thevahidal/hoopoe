from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as BaseTokenObtainPairSerializer,
)

from users.models import Driver, Organization, Recipient, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    image_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "image_thumbnail",
        ]


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            
            "profile",
        ]


class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["user"] = UserSerializer(user).data

        return token


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
        ]
        extra_kwargs = {
            "email": {
                "required": True,
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that email already exists.",
                    )
                ],
            }
        }


class OrganizationsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Organization
        fields = ["uuid", "name", "user", "is_personal", "image_thumbnail"]
        extra_kwargs = {
            "uuid": {
                "read_only": True,
            }
        }



class DriversSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Driver
        fields = ["type", "account_id", "active", "created_at", "updated_at"]


class RecipientsSerializer(serializers.ModelSerializer):
    drivers = DriversSerializer(many=True)
    image_thumbnail = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Recipient
        fields = ["username", "image_thumbnail", "name", "organization", "drivers", "active", "created_at", "updated_at"]

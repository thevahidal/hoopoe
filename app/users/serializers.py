from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import Organization

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password', ]
        extra_kwargs = {
            "email": {
                "required": True,
                "validators": [UniqueValidator(queryset=User.objects.all(), message="A user with that email already exists.")]
            }
        }
        

class OrganizationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Organization
        fields = ['name', 'user', ]
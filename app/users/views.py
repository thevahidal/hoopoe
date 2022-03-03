from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from users.models import Organization, OrganizationAPIKey
from users.serializers import (
    OrganizationSerializer,
    RegisterSerializer,
    TokenObtainPairSerializer,
)
from users.utils import get_tokens_for_user

from rest_framework_simplejwt.views import (
    TokenObtainPairView as BaseTokenObtainPairView,
)


class TokenObtainPairView(BaseTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class RegisterView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []
    authentication_classes = []

    def create(self, request):
        data = request.data.copy()

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        password = data.pop("password")
        user = serializer.save()
        user.set_password(password)
        user.save()

        organization = Organization.objects.create(user=user, is_personal=True)

        token = get_tokens_for_user(user)

        return Response(
            {
                "error": None,
                "message": "User successfully created.",
                "data": {
                    **token,
                    "organization": OrganizationSerializer(organization).data,
                },
            },
        )


class OrganizationView(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        name = data.pop("name")
        organization = serializer.save()
        api_key, key = OrganizationAPIKey.objects.create_key(
            name=name, organization=organization
        )

        return Response(
            {
                "data": {
                    **serializer.data,
                    "api_key": key,
                }
            },
            status=status.HTTP_201_CREATED,
        )

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset

from cgitb import lookup
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from users.models import Organization, OrganizationAPIKey, Recipient
from users.serializers import (
    OrganizationsSerializer,
    RecipientsSerializer,
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
                    "organization": OrganizationsSerializer(organization).data,
                },
            },
        )


class OrganizationsView(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "uuid"

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


class RecipientsView(ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "username"

    def get_queryset(self):
        user = self.request.user
        organization_uuid = self.kwargs.get("organization_uuid")        
        organization = get_object_or_404(
            Organization, uuid=organization_uuid, user=user
        )
        
        queryset = self.queryset.filter(organization=organization)
        return queryset

    def create(self, request, *args, **kwargs):
        organization_uuid = kwargs.get("organization_uuid")
        # organization = get_object_or_404(
        #     Organization, uuid=organization_uuid, user=request.user
        # )

        serializer = self.get_serializer(
            data={**request.data, "organization": organization_uuid}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        # organization_uuid = kwargs.get("organization_uuid")
        # get_object_or_404(Organization, uuid=organization_uuid, user=request.user)

        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

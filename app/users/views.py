from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from hoopoe.permissions import IsOwnerOrReadonly

from users.models import Organization, OrganizationAPIKey
from users.serializers import OrganizationSerializer, RegisterSerializer, UpdateOrganizationSerializer
from users.utils import get_tokens_for_user


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

        token = get_tokens_for_user(user)

        return Response(
            {"error": None, "message": "User successfully created.", "data": {**token}}
        )


class OrganizationView(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrReadonly]
    lookup_field = "uuid"
    
    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return UpdateOrganizationSerializer
        else:
            return OrganizationSerializer

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
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
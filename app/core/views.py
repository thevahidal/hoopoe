
from django.utils import timezone

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from rest_framework_api_key.permissions import HasAPIKey

from users.models import OrganizationAPIKey

from core.tasks import handle_send_upupa
from core.serializers import UpupaSerializer

class Timestamp(GenericViewSet):
    def retrieve(self, request, *args, **kwargs):
        now = timezone.now()
        beautified = now.strftime("%a, %b %d, %Y, %I:%M %p %Z")
        
        return Response(
            {
                "message": beautified,
                "error": None,
                "payload": {
                    "timestamp": now, 
                    "version": request.version
                }
            }
        )


class Upupa(GenericViewSet):
    serializer_class = UpupaSerializer
    # permission_classes = [HasAPIKey]

    def create(self, request, *args, **kwargs):
              
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        key = request.META["HTTP_X_API_KEY"].split()[1]
        api_key = OrganizationAPIKey.objects.get_from_key(key)
        organization = api_key.organization
        
        message = request.data.get("message")
  
        now = timezone.now()
        context = {
            "timestamp": now.strftime("%a, %b %d, %Y, %I:%M %p %Z"),
            "organization": organization.name,
            "message": message,
            "extra": request.data.get("extra", {}),
        }

        handle_send_upupa.delay(organization_id=organization.id, context=context)
        
        return Response(
            {
                "message": "Upupa sent successfully.",
                "error": None,
                "payload": {
                    "organization": api_key.organization.name
                },
            }
        )

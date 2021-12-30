from django.conf import settings

from rest_framework.permissions import BasePermission

from users.models import OrganizationAPIKey

class HasAPIKey(BasePermission):
    def has_permission(self, request, view):
        try:
            api_key_custom_header = getattr(settings, "API_KEY_CUSTOM_HEADER", None)
            key = request.META[api_key_custom_header]
            OrganizationAPIKey.objects.get_from_key(key)

            return True
        
        except:
            return False
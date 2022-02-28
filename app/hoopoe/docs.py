from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Hoopoe API",
        default_version="v1",
        description="",
        terms_of_service="https://www.hoopoe.app/terms/",
        contact=openapi.Contact(email="contact@hoopoe.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

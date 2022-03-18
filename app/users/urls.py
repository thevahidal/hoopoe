from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from users.views import OrganizationsView, RecipientsView, RegisterView, TokenObtainPairView

urlpatterns = [
    path("auth/token/obtain/", TokenObtainPairView.as_view(), name="token-obtain"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path(
        "auth/register/",
        RegisterView.as_view(
            {
                "post": "create",
            }
        ),
        name="register-view",
    ),
    path(
        "organizations/",
        OrganizationsView.as_view({"post": "create", "get": "list"}),
        name="organizations-view",
    ),
    path(
        "organizations/<str:uuid>/",
        OrganizationsView.as_view({"patch": "partial_update"}),
        name="organizations-detail-view",
    ),
    path(
        "organizations/<str:organization_uuid>/recipients/",
        RecipientsView.as_view({"post": "create", "get": "list"}),
        name="organizations-view",
    ),
    path(
        "organizations/<str:organization_uuid>/recipients/<str:username>/",
        RecipientsView.as_view({"post": "create", "get": "list"}),
        name="organizations-view",
    ),
]

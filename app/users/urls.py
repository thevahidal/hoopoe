from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import OrganizationView, RegisterView

urlpatterns = [
    path('auth/token/obtain/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    
    path('auth/register/', RegisterView.as_view({
        "post": "create",    
    }), name='register-view'),
    
    
    path('organizations/', OrganizationView.as_view({
        "post": "create",
        "get": "list",
    }), name="organizations-view"),
    path('organizations/<str:uuid>/', OrganizationView.as_view({
        "patch": "partial_update",
    }), name="organizations-details-view")
]
from django.urls import path

from core.views import SendUpupaView, TimestampView, UpupaView

urlpatterns = [
    path('organizations/<str:organization_uuid>/upupa/', UpupaView.as_view({
        "get": "list",
    }), name='upupa'),
    path('upupa/<str:uuid>/', UpupaView.as_view({
        "get": "retrieve",
    }), name='upupa-detail'),
    
    path('upupa/', SendUpupaView.as_view({
        "post": "create"
    }), name='send-upupa'),
    
    path('timestamp/', TimestampView.as_view({"get": "retrieve"}), name='timestamps'),
]

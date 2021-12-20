from django.urls import path

from core.views import Echo, Timestamp

urlpatterns = [
    
    path('echo/', Echo.as_view({"get": "retrieve"}), name='echo'),
    path('timestamp/', Timestamp.as_view({"get": "retrieve"}), name='timestamps'),
]

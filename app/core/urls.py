from django.urls import path

from core.views import Upupa, Timestamp

urlpatterns = [
    path('upupa/', Upupa.as_view({"post": "create"}), name='upupa'),
    
    path('timestamp/', Timestamp.as_view({"get": "retrieve"}), name='timestamps'),
]

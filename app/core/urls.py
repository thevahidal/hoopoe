from django.urls import path

from core.views import Dispatch, Timestamp

urlpatterns = [
    path('dispatch/', Dispatch.as_view({"post": "create"}), name='dispatch'),
    
    path('timestamp/', Timestamp.as_view({"get": "retrieve"}), name='timestamps'),
]


from rest_framework import permissions

UNSAFE_METHODS = [
    "PUT", "PATCH", "DELETE"
]

class IsOwnerOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in UNSAFE_METHODS:
            return obj.user == request.user
        return True
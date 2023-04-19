"""General permissions"""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsObjectOwner(BasePermission):
    """Allow access only to objects owned by the requesting user."""

    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        return request.user == obj.user


class IsStaff(BasePermission):
    """Allow access only if requesting user is staff."""

    def has_permission(self, request, view):
        return request.user.is_staff

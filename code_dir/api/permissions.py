from rest_framework import permissions


class IsAdminOrDoctor(permissions.BasePermission):
    """Allow access only to users with the 'doctor' role."""

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role in ["admin", "doctor"]

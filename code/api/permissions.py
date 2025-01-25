from rest_framework import permissions

class IsDoctor(permissions.BasePermission):
    """Allow access only to users with the 'doctor' role."""
    def has_permission(self, request, view):
        return request.user.role == 'doctor'
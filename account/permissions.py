from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return (request.user.role == 1)


class IsUserAdmin(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return (request.user.role == 2) or (request.user.role == 1)


class IsUserEmployee(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return (request.user.role == 3) or (request.user.role == 2) or (request.user.role == 1)

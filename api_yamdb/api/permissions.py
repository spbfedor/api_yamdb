from rest_framework import permissions

from users.models import ROLES


class IsAdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.role == ROLES.admin.name
            or request.user.is_superuser
        )


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        # Read permissions are allowed to any request but other
        # only to the admin user
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_anonymous:
            return False

        return (
            request.user.role == ROLES.admin.name
            or request.user.is_superuser
        )


class AuthorPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.role == ROLES.moderator.name
        )

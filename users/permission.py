from rest_framework import permissions


class ModerPermission(permissions.BasePermission):
    message = 'У вас нехватает прав'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False

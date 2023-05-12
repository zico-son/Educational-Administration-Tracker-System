from rest_framework import permissions


class CurrentUserOrSystemAdmin(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.role == 'system_admin' or obj.pk == user.pk
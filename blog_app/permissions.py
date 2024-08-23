from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        # Allowing any user to do get operation
        if request.method == "GET":
            return True
       # For other operations user must be is_staff
        return bool(request.user and request.user.is_staff)


class IsOwnerOrAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        # Allowing any user to do get operation
        if request.method in "GET":
            return True
        # For other operations user must be logged in
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Allowing only get method even if the user logged in
        if request.method in "GET":
            return True
        # Allowing any operations if the user is the owner or is_staff
        return bool(request.user and (request.user == obj.user or request.user.is_staff))

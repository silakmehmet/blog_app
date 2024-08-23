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
        if request.method == "GET":
            return True
        # For other operations user must be logged in
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            # Allowing viewing published blogs for all users
            if obj.status == 'p':
                return True
            # Allowing owners to view draft blogs
            return request.user == obj.user

        # Allowing other methods only if the user is the owner or an admin
        return bool(request.user and (request.user == obj.user or request.user.is_staff))

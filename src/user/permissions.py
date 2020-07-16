from rest_framework import permissions


class UpdateOwnDetail(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


# class PostOwnStatus(permissions.BasePermission):
#     """Allow users to update their own profile."""

#     def has_object_permission(self, request, view, obj):
#         """Check the user is trying to update their own status."""

#         if request.method in permissions.SAFE_METHODS:
#             return True

#         return obj.user_profile.id == request.user.id

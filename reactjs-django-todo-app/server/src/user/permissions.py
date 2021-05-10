import json
from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class RetriveOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # print(dir(view))
        return obj.id == request.user.id


class IsSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("Checking SuperUser")
        print(view.action)
        if view.action == "list":
            return request.user.is_superuser
        return True

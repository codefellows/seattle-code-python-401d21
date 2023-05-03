from rest_framework.permissions import BasePermission, SAFE_METHODS


class isOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if obj.owner is None:
            return True

        return obj.owner == request.user


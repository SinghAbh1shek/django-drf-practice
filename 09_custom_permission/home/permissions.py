from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsProductOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsVipUser(BasePermission):
    message = "Only VIP users are allowed to perform this action."
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, "userextended") and
            request.user.userextended.is_vip
        )
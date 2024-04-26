from rest_framework.permissions import BasePermission, SAFE_METHODS
from content.models import BlogPost


class BlogPostPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method not in SAFE_METHODS
            and request.user
            and request.user.authenticated
            and obj.user == request.user
        )

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ 判断是否是当前登录的用户 """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
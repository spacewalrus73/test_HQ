from rest_framework import permissions
from products.models import Access


class LessonAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return Access.objects.filter(
            product=view.kwargs["pk"],
            student=request.user.pk,
        )

from rest_framework import viewsets
from courses.models import Courses
from courses.serializers import CoursesSerializer, CoursesDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView

from users.permission import ModerPermission, IsOwner


class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesDetailSerializer
    queryset = Courses.objects.all()

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~ModerPermission,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (ModerPermission | IsOwner,)
        elif self.permission_classes == 'destroy':
            self.permission_classes = (~ModerPermission | IsOwner,)
        return super().get_permissions()

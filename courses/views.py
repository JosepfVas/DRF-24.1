from rest_framework import viewsets
from courses.models import Courses
from courses.paginators import CustomPagination
from courses.serializers import CoursesSerializer, CoursesDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from users.permission import ModerPermission, IsOwner


class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesDetailSerializer
    queryset = Courses.objects.all()
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~ModerPermission, IsAuthenticated)
        elif self.action in ['update', 'retrieve', 'list']:
            self.permission_classes = (IsAuthenticated, ModerPermission | IsOwner,)
        elif self.permission_classes == 'destroy':
            self.permission_classes = (IsAuthenticated, ~ModerPermission | IsOwner,)
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='moders').exists():
            # Модераторы видят все курсы.
            return Courses.objects.all()
        else:
            # Обычные пользователи видят только свои курсы.
            return Courses.objects.filter(owner=user)

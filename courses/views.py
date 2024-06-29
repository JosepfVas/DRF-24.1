from rest_framework import viewsets
from courses.models import Courses
from courses.paginators import CustomPagination
from courses.serializers import CoursesSerializer, CoursesDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from courses.tasks import send_course_update_email
from subscriptions.models import Subscription
from users.permission import ModerPermission, IsOwner
from rest_framework.response import Response


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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        subs = Subscription.objects.filter(course=instance)
        for sub in subs:
            user = sub.user
            send_course_update_email.delay(user.email, instance.title)

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()



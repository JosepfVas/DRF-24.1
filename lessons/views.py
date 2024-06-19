from rest_framework import generics
from lessons.models import Lessons
from lessons.serializers import LessonsSerializer
from rest_framework.permissions import IsAuthenticated

from lessons.permission import ModerPermission, IsOwner


class LessonsCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonsSerializer
    permission_classes = (IsAuthenticated, ~ModerPermission)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonsListAPIView(generics.ListAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated, ModerPermission | IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='moders').exists():
            # Модераторы видят все уроки
            return Lessons.objects.all()
        else:
            # Обычные пользователи видят только свои уроки
            return Lessons.objects.filter(owner=user)


class LessonsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated, ModerPermission | IsOwner]


class LessonsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated, ModerPermission | IsOwner]


class LessonsDeleteAPIView(generics.DestroyAPIView):
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated, ~ModerPermission | IsOwner]

from rest_framework import generics
from lessons.models import Lessons
from lessons.serializers import LessonsSerializer


class LessonsCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonsSerializer


class LessonsListAPIView(generics.ListAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class LessonsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class LessonsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class LessonsDeleteAPIView(generics.DestroyAPIView):
    queryset = Lessons.objects.all()

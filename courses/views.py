from rest_framework import viewsets
from courses.models import Courses
from courses.serializers import CoursesSerializer, CoursesDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView


class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesDetailSerializer
    queryset = Courses.objects.all()


    # def list(self, request):
    #     queryset = Courses.objects.all()
    #     serializer = CoursesListSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    #
    # def retrieve(self, request, pk=None, *args, **kwargs):
    #     queryset = Courses.objects.all()
    #     lessons = get_object_or_404(queryset, pk=pk)
    #     serializer = CoursesDetailSerializer(lessons)
    #     return Response(serializer.data)


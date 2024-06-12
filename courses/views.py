from rest_framework import viewsets
from courses.models import Courses
from courses.serializers import CoursesSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()

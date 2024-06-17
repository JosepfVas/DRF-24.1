from rest_framework import serializers
from courses.models import Courses
from lessons.serializers import LessonsSerializer
from users.models import Payments


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class CoursesDetailSerializer(serializers.ModelSerializer):
    lessons = LessonsSerializer(many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Courses
        fields = ['id', 'title', 'lessons_count', 'lessons', 'owner']


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

from rest_framework import serializers
from courses.models import Courses
from lessons.serializers import LessonsSerializer
from subscriptions.models import Subscription
from users.models import Payments


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class CoursesDetailSerializer(serializers.ModelSerializer):
    lessons = LessonsSerializer(many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Courses
        fields = ['id', 'title', 'lessons_count', 'lessons', 'owner', 'is_subscribed']

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

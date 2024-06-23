from rest_framework import serializers
from lessons.models import Lessons
from lessons.validators import validate_forbidden_url


class LessonsSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[validate_forbidden_url], read_only=True)

    class Meta:
        model = Lessons
        fields = ['id', 'title', 'description', 'owner', 'video_url']
        read_only_fields = ['owner', 'video_url']

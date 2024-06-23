from rest_framework import serializers


def validate_forbidden_url(value):
    if not value.startswith('https://www.youtube.com/'):
        raise serializers.ValidationError('URL must start with https://www.youtube.com/')



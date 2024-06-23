from rest_framework.views import APIView
from rest_framework.response import Response

from courses.models import Courses
from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer
from django.shortcuts import get_object_or_404


class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = kwargs.get('course_id')
        course_item = get_object_or_404(Courses, id=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course_item)
        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
            # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'
            # Возвращаем ответ в API
        return Response({"message": message})

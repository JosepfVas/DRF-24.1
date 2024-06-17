from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny


# Payments Views
class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('payed_course', 'payed_lesson')
    ordering_fields = ['payment_date', 'payment_method']


# User Views
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class LessonsListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LessonsRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LessonsUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LessonsDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()

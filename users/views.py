from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from users.models import Payments
from users.serializers import PaymentsSerializer


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('payed_course', 'payed_lesson')
    ordering_fields = ['payment_date', 'payment_method']

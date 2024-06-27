from users.services import create_stripe_price, create_stripe_session
from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny


# Payments Views

class PaymentsCreateAPIView(CreateAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        # converted_amount = convert_rub_to_dollars(payment.amount)
        price = create_stripe_price(payment.amount)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


# User Views
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()

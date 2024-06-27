from django.urls import path
from rest_framework.permissions import AllowAny
from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter
from users.views import (PaymentsCreateAPIView, UserCreateAPIView, UserListAPIView, UserUpdateAPIView,
                         UserRetrieveAPIView, \
    UserDeleteAPIView)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = CoursesConfig.name

router = DefaultRouter()
# router.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = [
                  # user
                  path('register/', UserCreateAPIView.as_view(), name='register'),
                  path('list/', UserListAPIView.as_view(), name='user_list'),
                  path('update/', UserUpdateAPIView.as_view(), name='user_update'),
                  path('retrieve/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
                  path('delete/', UserDeleteAPIView.as_view(), name='user_delete'),
                  # payments

                  path('payments/create/', PaymentsCreateAPIView.as_view(), name='payments_create'),
                  # token
                  path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + router.urls

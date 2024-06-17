from django.urls import path
from rest_framework.permissions import AllowAny
from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter
from users.views import PaymentsViewSet, UserCreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = [
                  path('register/', UserCreateAPIView.as_view(), name='register'),
                  path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + router.urls

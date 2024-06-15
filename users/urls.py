from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter
from users.views import PaymentsViewSet

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = []+router.urls

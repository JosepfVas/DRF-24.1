from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter
from courses.views import CoursesViewSet

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')

urlpatterns = [

]+router.urls


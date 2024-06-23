from django.urls import path
from lessons.views import LessonsCreateAPIView, LessonsUpdateAPIView, LessonsListAPIView, LessonsRetrieveAPIView, \
    LessonsDeleteAPIView

urlpatterns = [
    path('lessons/create/', LessonsCreateAPIView.as_view(), name='lessons-create'),
    path('lessons/list/', LessonsListAPIView.as_view(), name='lessons-list'),
    path('lessons/retrieve/<int:pk>/', LessonsRetrieveAPIView.as_view(), name='lessons-retrieve'),
    path('lessons/update/<int:pk>/', LessonsUpdateAPIView.as_view(), name='lessons-update'),
    path('lessons/delete/<int:pk>/', LessonsDeleteAPIView.as_view(), name='lessons-delete'),

]

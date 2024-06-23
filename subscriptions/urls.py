from django.urls import path

from subscriptions.views import SubscriptionAPIView

urlpatterns = [

    path('subscribe/<int:course_id>/', SubscriptionAPIView.as_view(), name='subscribe'),

]


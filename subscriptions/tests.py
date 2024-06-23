from rest_framework.test import APITestCase
from django.urls import reverse
from courses.models import Courses
from lessons.models import Lessons
from subscriptions.models import Subscription
from users.models import User
from rest_framework import status


class SubscriptionsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(name='test', surname='testov', email='test@example.com')
        self.courses = Courses.objects.create(title='Test Courses', description='Test Courses', owner=self.user)
        self.lessons = Lessons.objects.create(title='testlesson', description='testlesson description', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscribe(self):
        """ Тест на добавление подписки. """
        url = reverse('subscriptions:subscribe', kwargs={'course_id': self.courses.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'подписка добавлена')
        self.assertEqual(Subscription.objects.count(), 1)

    def test_unsubscribe(self):
        """ Тест на удаление подписки. """
        Subscription.objects.create(user=self.user, course=self.courses)
        url = reverse('subscriptions:subscribe', kwargs={'course_id': self.courses.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'подписка удалена')
        self.assertEqual(Subscription.objects.count(), 0)

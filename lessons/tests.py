from rest_framework.test import APITestCase
from django.urls import reverse
from lessons.models import Lessons
from users.models import User
from rest_framework import status


class LessonsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(name='test', surname='testov', email='test@example.com')
        self.lessons = Lessons.objects.create(title='testlesson', description='testlesson description', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lessons_create(self):
        """ Тест на создание урока. """
        url = reverse('lessons:lessons-create')
        data = {
            'title': 'testlessoncreate',
            'description': 'testlessoncreate description',
        }
        response = self.client.post(url, data=data)
        self.assertEqual(Lessons.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lessons_retrieve(self):
        """ Тест на просмотр урока. """
        url = reverse('lessons:lessons-retrieve', kwargs={'pk': self.lessons.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lessons_update(self):
        """ Тест на редактирование урока. """
        url = reverse('lessons:lessons-update', kwargs={'pk': self.lessons.id})
        data = {
            'title': 'testlessonupdate2',
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), 'testlessonupdate2')

    def test_lessons_delete(self):
        """ Тест на удаление урока. """
        url = reverse('lessons:lessons-delete', kwargs={'pk': self.lessons.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lessons.objects.all().count(), 0)

    def test_lessons_list(self):
        """ Тест на просмотр списка уроков. """
        url = reverse('lessons:lessons-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

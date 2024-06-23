from django.db import models
from config import settings


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey('courses.Courses', on_delete=models.CASCADE, verbose_name='курс')

    def __str__(self):
        return f'{self.user} {self.course}'

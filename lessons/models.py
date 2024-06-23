from django.db import models

from config import settings


class Lessons(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='lessons', null=True, blank=True, verbose_name='картинка')
    video_url = models.URLField(null=True, blank=True, verbose_name='ссылка на видео')
    course = models.ForeignKey('courses.Courses', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='lessons')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


from django.db import models
from courses.models import Courses
from users.models import NULLABLE


class Lessons(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='lessons', **NULLABLE, verbose_name='картинка')
    video_url = models.URLField(**NULLABLE, verbose_name='ссылка на видео')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
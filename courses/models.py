from django.db import models
from users.models import NULLABLE


class Courses(models.Model):
    title = models.CharField(max_length=150, verbose_name='название курса')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='courses', **NULLABLE)

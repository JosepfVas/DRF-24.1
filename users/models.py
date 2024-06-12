from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100, verbose_name='имя')
    surname = models.CharField(max_length=100, verbose_name='фамилия')
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.PositiveIntegerField(**NULLABLE, verbose_name='телефон')
    city = models.CharField(max_length=100, verbose_name='город')
    avatar = models.ImageField(upload_to='users', **NULLABLE, verbose_name='фото')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'P{self.email} {self.name} {self.surname} {self.city} {self.phone}'

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100, verbose_name='имя')
    surname = models.CharField(max_length=100, verbose_name='фамилия')
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.PositiveIntegerField(**NULLABLE, verbose_name='телефон')
    city = models.CharField(max_length=100, **NULLABLE, verbose_name='город')
    avatar = models.ImageField(upload_to='users', **NULLABLE, verbose_name='фото')
    last_login = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='последний раз в сети')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'P{self.email} {self.name} {self.surname} {self.city} {self.phone} {self.last_login}'


class Payments(models.Model):
    CASH = 'cash'
    BANK_TRANSFER = 'bank_transfer'

    PAYMENT_METHOD_CHOICES = [
        (CASH, 'Наличные'),
        (BANK_TRANSFER, 'Перевод на счет'),
    ]

    user = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
    payed_course = models.ForeignKey('courses.Courses', null=True, blank=True, on_delete=models.CASCADE,
                                     verbose_name='оплаченный курс')
    payed_lesson = models.ForeignKey('lessons.Lessons', null=True, blank=True, on_delete=models.CASCADE,
                                     verbose_name='оплаченный урок')
    amount = models.PositiveIntegerField(blank=True, null=True, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES, verbose_name='способ оплаты')
    session_id = models.CharField(max_length=400, blank=True, null=True, verbose_name='ID сессии')
    link = models.URLField(max_length=400, blank=True, null=True, verbose_name='ссылка на оплату')

    def __str__(self):
        return f'{self.user.name} - {self.amount}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

from django.core.mail import send_mail
from celery import shared_task
from config.settings import EMAIL_HOST_USER
from courses.models import Courses
from subscriptions.models import Subscription


@shared_task
def send_course_update_email(email, course_title):
    send_mail(
        'Обновление Курса',
        f"Ваш Курс {course_title} на который вы подписаны был обновлен!",
        EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

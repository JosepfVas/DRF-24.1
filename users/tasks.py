from celery import shared_task
from django.utils import timezone
from datetime import timezone, datetime, timedelta
from users.models import User


@shared_task
def deactivate_inactive_users():
    active_users = User.objects.filter(is_active=True)
    now = datetime.now(timezone.utc)
    for user in active_users:
        if user.last_login:
            if now - user.last_login > timedelta(days=30):
                user.is_active = False
                user.save()
                print(f"Пользователь {user} заблокирован")

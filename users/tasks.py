from datetime import timedelta, timezone

from celery import shared_task

from users.models import User


@shared_task
def disactive_users():
    users = User.objects.filter(is_active=True)
    for user in users:
        if user.last_login is None:
            break
        else:
            if timezone.now() - user.last_login > timedelta(days=30):
                user.is_active = False
                user.save()

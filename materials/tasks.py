from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_info_about_update_course(email):
    send_mail(
        "Обновление курса", "Произошло обновление курса", EMAIL_HOST_USER, [email]
    )


@shared_task
def test_function():
    print("hellow")


@shared_task
def disactive_users():
    users = User.objects.filter(is_active=True)
    for user in users:
        if datetime.now() - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()

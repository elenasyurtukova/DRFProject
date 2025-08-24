from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(
        max_length=15,
        verbose_name="телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите свое фото",
    )
    city = models.TextField(
        max_length=15,
        verbose_name="город",
        blank=True,
        null=True,
        help_text="Введите из какого вы города",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    cash = "Наличные"
    transfer = "Перевод на счет"
    method_payment_choices = [(cash, "Наличные"), (transfer, "Перевод на счет")]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        null=True,
        blank=True,
    )
    date_payment = models.DateField(verbose_name="дата оплаты")
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="купленный курс",
        null=True,
        blank=True,
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="купленный урок",
        null=True,
        blank=True,
    )
    sum_payment = models.FloatField(verbose_name="сумма оплаты")
    method_payment = models.CharField(
        max_length=30,
        choices=method_payment_choices,
        default="Наличные",
        verbose_name="способ оплаты",
    )

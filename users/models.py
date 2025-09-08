from django.contrib.auth.models import AbstractUser
from django.db import models


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
        on_delete=models.SET_NULL,
        verbose_name="пользователь",
        null=True,
        blank=True,
    )
    date_payment = models.DateTimeField(verbose_name="дата оплаты")
    course = models.ForeignKey(
        "materials.Course",
        on_delete=models.CASCADE,
        verbose_name="купленный курс",
        null=True,
        blank=True,
    )
    lesson = models.ForeignKey(
        "materials.Lesson",
        on_delete=models.CASCADE,
        verbose_name="купленный урок",
        null=True,
        blank=True,
    )
    sum_payment = models.PositiveIntegerField(verbose_name="сумма оплаты")
    method_payment = models.CharField(
        max_length=30,
        choices=method_payment_choices,
        default="Наличные",
        verbose_name="способ оплаты",
    )
    session_id = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="id сессии"
    )
    link = models.URLField(
        max_length=400, blank=True, null=True, verbose_name="Ссылка на оплату"
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return self.sum_payment

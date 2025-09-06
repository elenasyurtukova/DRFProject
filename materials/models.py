from django.db import models

from config.settings import AUTH_USER_MODEL


class Course(models.Model):
    title_course = models.CharField(max_length=50, verbose_name="название курса")
    image_course = models.ImageField(
        upload_to="materials/images/",
        blank=True,
        null=True,
        verbose_name="превью курса",
    )
    description_course = models.TextField(
        blank=True, null=True, verbose_name="Описание"
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="владелец",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["title_course"]

    def __str__(self):
        return self.title_course


class Lesson(models.Model):
    title_lesson = models.CharField(max_length=50, verbose_name="название урока")
    image_lesson = models.ImageField(
        upload_to="materials/images/",
        blank=True,
        null=True,
        verbose_name="превью урока",
    )
    description_lesson = models.TextField(
        blank=True, null=True, verbose_name="Описание"
    )
    video_link = models.URLField(
        blank=True, null=True, verbose_name="ссылка на видео урока"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="курс",
        null=True,
        blank=True,
        related_name="lessons",
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="владелец",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["title_lesson", "course"]

    def __str__(self):
        return self.title_lesson


class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
        blank=True, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'Подписка на курс {self.course}'

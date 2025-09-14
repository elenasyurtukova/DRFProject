from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.user.set_password("0147")
        self.client.force_authenticate(user=self.user)  # авторизуем пользователя
        self.course = Course.objects.create(
            title_course="test_course_1", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title_lesson="test_lesson_1",
            course=self.course,
            owner=self.user,
            video_link="http://yuotube.com/video/ghfjgbkjbg",
        )

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title_lesson"), self.lesson.title_lesson)

    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {
            "title_lesson": "test_lesson_2",
            "course": self.course.pk,
            "owner": self.user.pk,
            "video_link": "https://youtube.com/video/8390046444092808726",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {
            "title_lesson": "test_lesson_01",
            "video_link": "https://youtube.com/video/8390046444092808726",
        }
        response = self.client.patch(url, data)
        data = response.json()
        print("\ntest_lesson_update")
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title_lesson"), "test_lesson_01")

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        # self.lesson.owner = self.user
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("materials:lessons_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.all().count(), 1)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.user.set_password("0147")
        self.client.force_authenticate(user=self.user)  # авторизуем пользователя
        self.course = Course.objects.create(
            title_course="test_course_1", owner=self.user
        )

    def test_subscribe(self):
        url = reverse("materials:subscribe")
        data = {"id": self.course.pk}
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {"message": "Подписка добавлена"})

    def test_unsubscribe(self):
        url = reverse("materials:subscribe")
        data = {"id": self.course.pk}
        self.client.post(url, data)
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {"message": "Подписка удалена"})

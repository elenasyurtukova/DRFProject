from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner

from .models import Lesson


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serialazer):
        """метод автоматического сохранения пользователя в поле владельца"""
        course = serialazer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        """метод распределения прав доступа"""
        if self.action == "create":
            self.permission_classes = (~IsModerator,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsOwner | ~IsModerator,)
        return super().get_permissions()

    def get_queryset(self):
        if self.request.user.is_staff == True:
            return Course.objects.all()
        return Course.objects.filter(owner=self.request.user)

class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator, IsAuthenticated)


    def perform_create(self, serialazer):
        """метод автоматического сохранения пользователя в поле владельца"""
        lesson = serialazer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)

    def get_queryset(self):
        if self.request.user.is_staff == True:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModerator | IsOwner,)

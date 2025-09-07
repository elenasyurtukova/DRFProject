from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.urls import app_name

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateApiView,
                             LessonDestroyApiView, LessonListApiView,
                             LessonRetrieveApiView, LessonUpdateApiView,
                             SubscriptionCreateApiView)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path(
        "lessons/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson_delete"
    ),
    path(
        "lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson_update"
    ),
    path("subscribe/", SubscriptionCreateApiView.as_view(), name="subscribe"),
]
urlpatterns += router.urls

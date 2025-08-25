from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class LessonShortSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            "id",
            "title_lesson",
            "description_lesson",
        )


class CourseSerializer(ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonShortSerializer(many=True, read_only=True)

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = "__all__"

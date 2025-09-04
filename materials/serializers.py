from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscription
from materials.validators import LessonVideo_linkValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LessonVideo_linkValidator(field='video_link')]


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

class SubscriptionSerializer(ModelSerializer):
    subscription_status = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = "__all__"

    def get_subscription_status(self, obj):
        if obj.is_active==True:
            return 'подписка активна'
        else:
            return 'подписка удалена'



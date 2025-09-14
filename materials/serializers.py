from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscription
from materials.validators import LessonVideo_linkValidator
from users.serializers import UserSerializer


class LessonSerializer(ModelSerializer):
    video_link = serializers.CharField(validators=[LessonVideo_linkValidator()])

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
    subscription = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_subscription(self, obj):
        user = obj.owner
        return Subscription.objects.all().filter(user=user).filter(course=obj).exists()

    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = "__all__"

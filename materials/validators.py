import re

from rest_framework.serializers import ValidationError


class LessonVideo_linkValidator:
    @classmethod
    def __fields__(cls):
        return ['video_link']

    def __call__(self, value):
        pattern = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/'
        if not re.search(pattern, value):
            raise ValidationError("Invalid video link! Must be a valid YouTube URL.")

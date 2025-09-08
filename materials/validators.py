from rest_framework.serializers import ValidationError


class LessonVideo_linkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        our_string = "http://yuotube.com/"
        our_value = dict(value).get(self.field)
        if our_string not in str(our_value):
            raise ValidationError("Your video_link is wrong")

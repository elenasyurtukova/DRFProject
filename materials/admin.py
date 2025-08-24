from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title_course", "description_course")
    list_filter = ("title_course", "description_course")
    search_fields = ("title_course", "description_course")

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title_lesson", "description_lesson", "course")
    list_filter = ("title_lesson", "description_lesson", "course")
    search_fields = ("title_lesson", "description_lesson", "course")

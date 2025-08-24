from django.contrib import admin
from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date_payment", "course", "lesson", "sum_payment", "method_payment")
    list_filter = ("user", "date_payment", "course", "lesson", "sum_payment", "method_payment")
    search_fields = ("user", "date_payment", "course", "lesson", "sum_payment", "method_payment")
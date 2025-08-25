from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentListAPIView, PaymentUpdateApiView

app_name = UsersConfig.name

urlpatterns = [
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
    path("payment/<int:pk>/update/", PaymentUpdateApiView.as_view(), name="payment_update"),
]

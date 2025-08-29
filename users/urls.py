from django.urls import path
from rest_framework_simplejwt.views import (
TokenObtainPairView, TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import PaymentListAPIView, PaymentUpdateApiView

app_name = UsersConfig.name

urlpatterns = [
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
    path(
        "payment/<int:pk>/update/",
        PaymentUpdateApiView.as_view(),
        name="payment_update",
    ),
    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]

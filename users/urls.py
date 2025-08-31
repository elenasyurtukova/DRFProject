from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentListAPIView, PaymentUpdateApiView,
                         UserCreateApiView)

app_name = UsersConfig.name

urlpatterns = [
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
    path(
        "payment/<int:pk>/update/",
        PaymentUpdateApiView.as_view(),
        name="payment_update",
    ),
    path("register/", UserCreateApiView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]

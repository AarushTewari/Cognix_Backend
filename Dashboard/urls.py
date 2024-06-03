from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"chat_request", ChatRequestViewset, basename = "chat_request")

urlpatterns = [
    path("", Index.as_view(), name='index'),
    path("login/", UserLoginView.as_view(), name='login'),
    path("token/", TokenRefreshView.as_view(), name='token_refresh'),
    path("logout/", UserLogoutView.as_view(), name='logout'),
    path("", include(router.urls)),
]

from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"chat_request", ChatRequestViewset, basename = "chat_request")

urlpatterns = [
    path("", Index.as_view(), name='index'),
    path("login/", UserLoginView.as_view(), name='login'),
    path("logout/", UserLogoutView.as_view(), name='logout'),
    path("", include(router.urls))
]

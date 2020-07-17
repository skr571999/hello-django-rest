# from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import UserViewSet
from .views import UserRegistrationAPIView

router = DefaultRouter()
router.register('user', UserViewSet)

# urlpatterns = [
#     path("register/", UserRegistrationAPIView.as_view()),
# ]

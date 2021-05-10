from rest_framework.routers import DefaultRouter

from .views import UserViewSet, LoginViewSet

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('login', LoginViewSet, basename="login")

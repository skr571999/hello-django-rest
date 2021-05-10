from rest_framework.routers import DefaultRouter

from .views import TodoAPIViewSet

router = DefaultRouter()
router.register('todo', TodoAPIViewSet)

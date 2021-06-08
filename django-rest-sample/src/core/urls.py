from django.urls import path, include

from core import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    # path('core/', views.send_token_view),
    # path('core/detail', views.get_detail_view),
    # path('core/users', views.UserViewSet.as_view()),
    # path('core/users/*', views.UserViewSet.as_view()),
]
urlpatterns += router.urls

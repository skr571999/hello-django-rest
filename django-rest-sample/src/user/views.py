from rest_framework.generics import CreateAPIView

from .serializers import UserRegistrationSerializer


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

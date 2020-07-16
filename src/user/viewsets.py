from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .models import User
from .permissions import UpdateOwnDetail


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # authentication_classes = ()
    permission_classes = (IsAuthenticated, UpdateOwnDetail)

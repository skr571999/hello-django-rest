from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .permissions import UpdateOwnProfile, RetriveOwnProfile, IsSuperUser


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        # IsSuperUser,
        UpdateOwnProfile,
        RetriveOwnProfile,
        IsAuthenticated)

    def get_permissions(self):
        print("CCCC")
        print(self.action)
        if self.action == 'list':
            permission_classes = self.permission_classes + (IsSuperUser,)
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    # def list(request, *args, **kwargs):
    #     return Response({'message': "List not Alloted"})


class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        print(ObtainAuthToken().post(request))
        return ObtainAuthToken().post(request)

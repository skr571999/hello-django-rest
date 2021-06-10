from django.shortcuts import render
from django.http.response import JsonResponse

from datetime import datetime, timedelta


from rest_framework import viewsets, serializers, generics, pagination, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'course']


def response_with_paginator(viewset, queryset):
    page = viewset.paginate_queryset(queryset)
    if page is not None:
        serializer = viewset.get_serializer(page, many=True)
        return viewset.get_paginated_response(serializer.data)

    return Response(viewset.get_serializer(queryset, many=True).data)


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, mixins.CreateModelMixin
                  ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPageNumberPagination

    @action(detail=False, methods=["GET"], url_path='get-users')
    def get_users(self, *args):
        queryset = self.get_queryset()
        return response_with_paginator(self, queryset)

from django.shortcuts import render
from django.http.response import JsonResponse

from datetime import datetime, timedelta


# import jwt


# users_mock_data = [
#     {
#         "id": 1,
#         "name": "Apple",
#         "expiration_date": "13-05-2021",
#     }
# ]


# def send_token_view(request):
#     encoded_jwt = jwt.encode(
#         {"user": "Apple", "device_id": "1234", "exp": datetime.utcnow() + timedelta(seconds=30)}, "APSJ12322@!", algorithm="HS256")
#     return JsonResponse({'message': "Success", "token": encoded_jwt.decode('utf-8')})


# def get_detail_view(request):
#     print(dir(request.headers))
#     print(request.headers.get('Authorization'))

#     return JsonResponse({'a': "a"})


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
    # pagination_class = pagination.PageNumberPagination
    pagination_class = CustomPageNumberPagination

    @action(detail=False, methods=["GET"], url_path='get-users')
    def get_users(self, *args):
        # response_data = self.get_serializer(self.get_queryset(), many=True).data
        # print("self.paginate_queryset",self.paginate_queryset)
        # return Response(response_data)
        queryset = self.get_queryset()

        return response_with_paginator(self, queryset)

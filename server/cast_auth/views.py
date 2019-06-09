__author__ = "RituRaj"


from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import parsers, renderers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serailizers import UserAuthTokenSerializer, UserSerializer

from .models import UserAuth


class UserAuthLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserAuthTokenSerializer(data=request.data)
        serialized_data = serializer.create_validate(request.data)
        user = serialized_data['user']
        if user:
            token, created = Token.objects.get_or_create(user=user)
            response = {
                'token': token.key,
                'status': 'normal',
                'is_staff': user.is_staff
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'token': None}, status=status.HTTP_400_BAD_REQUEST)


# User Registeration
class UserRegisterationView(APIView):
    permission_classes = ()
    parser_classes = (parsers.FormParser,
                      parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request, *args, **kwargs):
        # try:
        if True:
            serializer = UserSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                serialized_data = serializer.data
                username = serialized_data["name"]
                password = make_password(request.data["password"])
                with transaction.atomic():
                    django_user = User(username=username,
                                       password=password, is_staff=False)
                    django_user.save()
                    serialized_data["user_id"] = django_user.id
                    UserAuth.objects.create(**serialized_data)
                return Response({"success": True}, status=status.HTTP_200_OK)
            else:
                return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)

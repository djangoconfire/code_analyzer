__author__ = "RituRaj"


from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from django.contrib.auth import authenticate
from rest_framework.authtoken.serializers import AuthTokenSerializer

from django.contrib.auth.models import User
from .functions import check_credentials
from .models import UserAuth


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ["name", "email"]


class UserAuthTokenSerializer(AuthTokenSerializer):

    def create_validate(self, attrs):
        username = attrs.get('username')
        auth_obj = UserAuth.objects.get(name=username)
        username = auth_obj.user.username
        password = attrs.get('password')
        if username and password:
            user, is_authenticated = check_credentials(username, password)
            if user:  # username is correct
                if is_authenticated:
                    attrs['user'] = user
                    return attrs
                else:
                    msg = "User does not Exist"
                    raise serializers.ValidationError(msg)

            else:
                msg = "Unable to login with provided credentials"
                raise serializers.ValidationError(msg)

        else:
            msg = ('Must include username and password')
            raise serializers.ValidationError(msg)

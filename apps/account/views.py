from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from account.serializers import UserDetailSerializer

User = get_user_model()


class CustomBackend(ModelBackend):
    """ 自定义用户验证 """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 用户名和手机号都能登录
            user = User.objects.get(
                Q(username=username) | Q(mobile=username) | Q(name=username)
            )
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None


class UserViewset(viewsets.ModelViewSet):
    """ 用户详情 list 列表 """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_queryset(self):
        # query = Q(role=choices.Role.ROLE_JL) | Q(role=choices.Role.ROLE_ZG) | Q(role=choices.Role.ROLE_YW)
        queryset = User.objects.all()
        return queryset

    def get_object(self):
        return self.request.user

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (GenericAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.db import IntegrityError


from .serializers import (RegisterSerializer,
                          ChangePasswordSerializers,
                          LoginSerializer,
)
from .models import User, Phone
from .utils import Utils


class RegisterView(GenericAPIView):
    """ Вид регистрации пользователя """
    serializer_class = RegisterSerializer

    def post(self, request):
        if IntegrityError:
            pass
        user = request.data
        serializer = self.get_serializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        phone = Phone.objects.create(
            phone=user['phone'],
            user=User.objects.get(username=serializer.data['username'])
        )
        phone.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = self.get_serializer(data=user)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, username=serializer.data.get('username'), password=serializer.data.get('password'))
        tokens = Utils.get_token_for_user(user)
        if user is not None:
            if user.check_subscription_expiry:
                user.is_subscribed = False
                user.save()
                return Response({'message': _('Your subscribe expired'), 'tokens': tokens},
                                status=status.HTTP_200_OK)
            return Response({'message': _('Login Success'), 'tokens': tokens},
                            status=status.HTTP_200_OK)
        return Response({'message': _('Invalid credentials')}, status=status.HTTP_401_UNAUTHORIZED)


class ChangePasswordAPIView(UpdateAPIView):
    serializer_class = ChangePasswordSerializers
    model = User
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        data = request.data

        if serializer.is_valid():
            if not user.check_password(data.get("old_password")):
                return Response({'message': _("Wrong old password")}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(data.get("new_password"))
            user.save()
            return Response({'message': _("Password updated successfully")}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
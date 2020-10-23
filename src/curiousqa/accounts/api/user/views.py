from accounts.api.user.serializers import (
                                      AccountUserSerializer,
                                      ChangePasswordSerializer,
                                      ChangeEmailSerializer)
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.models import Account

class AccountUserView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """ Get the account data """
        account = request.user

        if account:
            account_serialized = AccountUserSerializer(account)
            return Response(account_serialized.data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid Auth'},
                        status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        """ Delete an account """
        account = request.user

        if account:
            account.delete()
            return Response({'detail': 'Deleted'}, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid Auth'},
                        status=status.HTTP_401_UNAUTHORIZED)


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request):
        account = request.user

        if account:
            serializer = ChangePasswordSerializer(data=request.data)
            if serializer.is_valid():
                if not account.check_password(
                        serializer.data.get("old_password")):
                    return Response({'detail': 'Incorrect Password'},
                                    status=status.HTTP_400_BAD_REQUEST)
                else:
                    account.set_password(serializer.data.get('new_password'))
                    account.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({'detail': 'Invalid Auth'},
                        status=status.HTTP_401_UNAUTHORIZED)


class ChangeEmailView(GenericAPIView):
    serializer_class = ChangeEmailSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request):
        account = request.user

        if account:
            serializer = ChangeEmailSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    queried_account = Account.objects.get(
                        email=serializer.data.get('email'))
                    return Response({'detail': 'A user with that email already exists.'},
                                    status=status.HTTP_400_BAD_REQUEST)
                except Account.DoesNotExist:
                    account.email = serializer.data.get('email')
                    account.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({'detail': 'Invalid Auth'},
                        status=status.HTTP_401_UNAUTHORIZED)

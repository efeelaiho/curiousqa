from accounts.api.authentications import get_expires_in, token_expire_handler
from accounts.api.serializers import (AccountRegistrationSerializer,
                                      AccountSerializer,
                                      AccountSignInSerializer)
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


class AccountRegisterView(GenericAPIView):
    serializer_class = AccountRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AccountRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account_serialized = AccountSerializer(account)
            token = Token.objects.get(user=account)

            return Response({
                'account': account_serialized.data,
                'token': token.key,
                'token_expires_in': get_expires_in(token)}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountSignInView(GenericAPIView):
    serializer_class = AccountSignInSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AccountSignInSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
        account = authenticate(
            password=serializer.data['password'],
            email=serializer.data['email'])

        if not account:
            # there is no account with these credentials / wrong password
            response_msg = 'Invalid Credentials or activate account'
            return Response({'detail': response_msg},
                            status=status.HTTP_404_NOT_FOUND)

        token, was_created = Token.objects.get_or_create(user=account)
        is_expired, token = token_expire_handler(token)
        account_serialized = AccountSerializer(account)

        return Response({
            'account': account_serialized.data,
            'token': token.key,
            'token_expires_in': get_expires_in(token)}, status=status.HTTP_200_OK)


class AccountSignOutView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class AccountsUserView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        account = request.user
        if account:
            data = {}
            data['account_id'] = account.account_id
            data['username'] = account.username
            data['email'] = account.email

            return Response(data, status=status.HTTP_200_OK)

        return Response({'response': 'Invalid Auth'},
                        status=status.HTTP_401_UNAUTHORIZED)

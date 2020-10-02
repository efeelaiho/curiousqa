from accounts.api.serializers import AccountRegistrationSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


# Create your views here.

class AccountRegisterView(GenericAPIView):
    serializer_class = AccountRegistrationSerializer
    def post(self, request):
        serializer = AccountRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.get(user=account).key
            data = dict(serializer.data)
            data['token']= token

            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountLoginView(GenericAPIView):
    def post(self, request):
        data = request.data

        username = data.get('username', '')
        password = data.get('password', '')

        pass  

        
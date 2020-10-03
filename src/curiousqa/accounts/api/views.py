from accounts.api.serializers import AccountRegistrationSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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

        return Response({'response': 'Invalid Auth'}, status=status.HTTP_401_UNAUTHORIZED)

        
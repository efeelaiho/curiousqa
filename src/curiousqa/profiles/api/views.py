from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from profiles.api.serializers import ProfilePublicSerializer, ProfileSerializer


class ProfileView(GenericAPIView):

    def get(self, request):
        pass

class ProfilePublicView(GenericAPIView):

    def get(self, request, username):
        pass

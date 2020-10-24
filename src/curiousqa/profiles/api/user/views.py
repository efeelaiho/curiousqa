from profiles.api.user.serializers import ProfileUserSerializer
from profiles.models import Profile
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProfileUserView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileUserSerializer

    def get(self, request):
        """ Get the profile data """
        account =  request.user

        if account:
            profile = Profile.objects.get(account=account)
            profile_serialized = ProfileUserSerializer(profile)

            return Response(profile_serialized.data, status=status.HTTP_200_OK)
        
        return Response({'detail': 'Invalid Auth'},
                        status=status.HTTP_401_UNAUTHORIZED)

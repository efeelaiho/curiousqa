from accounts.models import Account
from accounts.tests import APIAuthenticatedTest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.models import Profile


class ProfileUserViewTestCase(APIAuthenticatedTest):
    """
    Ensure we can perform rest method operations on profile instance
    """
    url = reverse('profiles_user:profile')

    def test_get_profile(self):
        response = self.client.get(path=self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

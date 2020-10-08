import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from accounts.api.serializers import AccountRegistrationSerializer
from accounts.models import Account


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        """
        Ensure we can create a new account object via registration.
        """
        data = {'username': 'testcase', 'email': 'testcase@curiousqa.com',
                'password': 'testcasePaSsW0rd123'}
        response = self.client.post(path='/accounts/auth/register', data=data)
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED,
            msg="Test Registration")


class SignInTestCase(APITestCase):
    """
    Ensure we can login an account and obtain an authentication token
    """

    def setUp(self):
        self.raw_password = 'testcasePaSsW0rdXYZ'
        self.account = Account.objects.create_user(
            email='testcase@curiousqa.com',
            username='testcase',
            password=self.raw_password)

    def test_signin(self):
        data = {'email': self.account.email, 'password': self.raw_password}
        response = self.client.post(path='/accounts/auth/signin', data=data)
        print(response.data)
        self.assertIn('token', response.data)
        self.assertIn('account', response.data)
        self.assertIn('token_expires_in', response.data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

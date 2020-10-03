from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from accounts.api.serializers import AccountRegistrationSerializer
from accounts.models import Account


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        pass
    
    def test_login_account(self):
        """
        Ensure we can login an account and obtain an authentication token
        """
        pass

        
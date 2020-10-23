import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from accounts.models import Account


class RegistrationTestCase(APITestCase):
    """
    Ensure we can create a new account object via registration.
    """
    url = reverse('accounts_auth:register')

    def test_registration(self):
        data = {'username': 'testcase', 'email': 'testcase@curiousqa.com',
                'password': 'testcasePaSsW0rd123'}
        response = self.client.post(path=self.url, data=data)
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED,
            msg="Test Registration")


class SignInTestCase(APITestCase):
    """
    Ensure we can login an account and obtain an authentication token
    """

    url = reverse('accounts_auth:signin')

    def setUp(self):
        self.raw_password = 'testcasePaSsW0rdXYZ'
        self.account = Account.objects.create_user(
            email='testcase@curiousqa.com',
            username='testcase',
            password=self.raw_password)

    def test_signin(self):
        data = {'email': self.account.email, 'password': self.raw_password}
        response = self.client.post(path=self.url, data=data)
        self.assertIn('token', response.data)
        self.assertIn('account', response.data)
        self.assertIn('token_expires_in', response.data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class SignOutTestCase(APITestCase):
    """
    Ensure we can logout an account and remove an authentication token
    """
    url = reverse('accounts_auth:signout')

    def setUp(self):
        self.raw_password = 'testcasePaSsW0rdXYZ'
        self.account = Account.objects.create_user(
            email='testcase_accountlo@curiousqa.com',
            username='testcase_accountlo',
            password=self.raw_password)

        # token already exists due to  generation of token on post_save of
        # Account object
        self.token = Token.objects.get(user=self.account)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(
                self.token.key))

    def test_signout(self):
        response = self.client.post(path=self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class AccountViewTestCase(APITestCase):
    """
    Ensure we can perform rest method operations on an account instance
    """

    def setUp(self):
        self.raw_password = 'testcasePaSsW0rdXYZ'
        self.account = Account.objects.create_user(
            email='testcase_accountview1@curiousqa.com',
            username='testcase_accountview1',
            password=self.raw_password)
        self.url = reverse('accounts_user:account')
        # token already exists due to  generation of token on post_save of
        # Account object
        self.token = Token.objects.get(user=self.account)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(
                self.token.key))

    def test_get_account(self):
        response = self.client.get(path=self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_account(self):
        account_deleted = False
        response = self.client.delete(path=self.url)
        try:
            account = Account.objects.get(account_id=self.account.account_id)
        except Account.DoesNotExist as adne:
            account_deleted = True

        self.assertTrue(account_deleted)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class AccountPasswordChangeTestCase(APITestCase):
    """
    Ensure we can change the password on an account instance
    """

    def setUp(self):
        self.original_password = 'a1b2c3d4e5f6g7'
        self.account = Account.objects.create_user(
            email='testcase_for_password@curiousqa.com',
            username='testcase_password',
            password=self.original_password)
        self.url = reverse('accounts_user:password')
        self.token = Token.objects.get(user=self.account)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(
                self.token.key))

    def test_password_change(self):
        data = {'old_password': self.original_password,
                'new_password': 'I_AM_A_NEW_PASSWORD1'}
        repsponse = self.client.put(path=self.url, data=data)
        self.assertEquals(repsponse.status_code, status.HTTP_204_NO_CONTENT)


class AccountEmailChangeTestCase(APITestCase):
    """
    Ensure we can change the email on an account instance

    """
    def setUp(self):
        self.original_password = 'a1b2c3d4e5f6g7'
        self.account = Account.objects.create_user(
            email='testcase_for_email@curiousqa.com',
            username='testcase_email',
            password=self.original_password)
        self.url = reverse('accounts_user:email')
        self.token = Token.objects.get(user=self.account)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(
                self.token.key))

    def test_email_change(self):
        data = {'email': 'new_email@curiousqa.com'}
        repsponse = self.client.put(path=self.url, data=data)
        self.assertEquals(repsponse.status_code, status.HTTP_204_NO_CONTENT)

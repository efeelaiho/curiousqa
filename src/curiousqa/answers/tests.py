
from accounts.models import Account
from django.test import TestCase
from django.urls import reverse
from questions.models import Question
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class AnswerTests(APITestCase):
    def test_create_answer(self):
        """
        Ensure we can create a new answer object.
        """
        pass

from accounts.models import Account
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from questions.models import Question


class QuestionTests(APITestCase):
    def test_create_question(self):
        """
        Ensure we can create a new question object.
        """
        pass
    
    
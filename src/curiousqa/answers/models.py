import base64
import uuid

from django.conf import settings
from django.db import models
from questions.models import Question


class Answer(models.Model):
    answer_id = models.CharField(
        max_length=32, editable=False, unique=True, 
        default=base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8').replace('=', ''))
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name="date published")
    answer = models.CharField(
        max_length=200, editable=False, null=False, blank=False)
    answer_details = models.TextField(
        blank=True, max_length=500, editable=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=False, null=True)

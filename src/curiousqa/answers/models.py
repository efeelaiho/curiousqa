from django.db import models
from django.conf import settings
from questions.models import Question
import uuid


class Answer(models.Model):
    answer_id = models.CharField(
        max_length=32, editable=False, unique=True, default=uuid.uuid4().hex)
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name="date published")
    answer = models.CharField(
        max_length=200, editable=False, null=False, blank=False)
    answer_details = models.TextField(
        blank=True, max_length=500, editable=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=False, null=True)

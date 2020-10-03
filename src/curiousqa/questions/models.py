from django.db import models
from django.conf import settings
import uuid

class Question(models.Model):
    question_id      = models.CharField(max_lenght=32, editable=False, unique=True, default=uuid.uuid4().hex)
    question_title   = models.CharField(max_lenght=100, editable=False, null=False, blank=False)
    question_details = models.TextField(blank=True, max_length=200, editable=False)
    date_published 	 = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    owner            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_answered      = models.BooleanField(default=False)
    

import base64
import uuid

from django.conf import settings
from django.db import models

class Profile(models.Model):
    profile_id = models.CharField(max_length=32, editable=False, unique=True, default=base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8').replace('=', ''))
    account = models.OneToOneField(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField()
    question_limit = models.IntegerField(default=50)
    no_questions_asked = models.IntegerField(default=0)
    no_questions_answered = models.IntegerField(default=0)




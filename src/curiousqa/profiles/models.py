import base64
import uuid

from django.conf import settings
from django.db import models


class Profile(models.Model):
    profile_id = models.CharField(
        max_length=32, editable=False, unique=True, 
        default=base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8').replace('=', ''))
    username = models.SlugField(max_length=50, unique=True, required=True)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='profiles', on_delete=models.CASCADE)
    avatar = models.ImageField()
    question_limit = models.IntegerField(default=25)
    


    
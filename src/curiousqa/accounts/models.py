import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username: 
            raise ValueError('Users must have a username')

        user = self.model (
            email=self.normalize_email(email),
            username=username,
    
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    account_id =  models.UUIDField(default=uuid.uuid4().hex, editable=False, unique=True)
    email      =  models.EmailField(verbose_name="email", max_length=255, unique=True)
    username   =  models.CharField(max_length=25, unique=True)

    is_staff	 = models.BooleanField(default=False)
    is_admin	 = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_active   = models.BooleanField(default=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name='last login', auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    # For checking permissions. all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        #"Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_authentication_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    pass

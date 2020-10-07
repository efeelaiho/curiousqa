from datetime import timedelta

from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


def get_expires_in(token):
    # get time remaining for token till it expires
    time_elapsed = timezone.now() - token.created
    time_allowed = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS)
    remaining_time = time_allowed - time_elapsed
    
    return remaining_time

def is_token_expired(token):
    return get_expires_in(token) <= timedelta(seconds=0)

def token_expire_handler(token):
    is_expired = is_token_expired(token)
    if is_expired:
        # if token is expired it will be romved and a new 
        # token (with a different key) will be established
        token.delete()
        token = Token.objects.create(user=token.user)
        
    return is_expired, token

class ExpiringTokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid Token')

        if not token.user.is_active:
            raise AuthenticationFailed('Account is not active')

        is_expired, token = token_expire_handler(token)

        if is_expired:
            raise AuthenticationFailed('The Token is expired')
        
        return (token.user, token)
    





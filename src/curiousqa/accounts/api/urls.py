from accounts.api.views import AccountRegisterView, AccountsUserView
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts'

urlpatterns = [
    path('auth/register', AccountRegisterView.as_view(), name='register'),
    path('auth/login', obtain_auth_token, name='login'),
    path('', AccountsUserView.as_view(), name='account'),
]


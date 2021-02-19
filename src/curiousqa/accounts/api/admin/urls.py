"""
from accounts.api.views import (AccountRegisterView, AccountSignInView,
                                AccountSignOutView, AccountsUserView,
                                ChangePasswordView, ChangeEmailView)
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('<str:account_id>', AccountsUserView.as_view(), name='account'),
    path('<str:account_id>/password', ChangePasswordView.as_view(), name='password'),
    path('<str:account_id>/email', ChangeEmailView.as_view(), name='email'),
    path('me', AccountsUserView.as_view(), name='account'),
    path('me/password', ChangePasswordView.as_view(), name='password'),
    path('me/email', ChangeEmailView.as_view(), name='email'),
]
"""
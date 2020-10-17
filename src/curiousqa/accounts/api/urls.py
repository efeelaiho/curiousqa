from accounts.api.views import (AccountRegisterView, AccountSignInView,
                                AccountSignOutView, AccountsUserView,
                                ChangePasswordView, ChangeEmailView)
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('auth/register', AccountRegisterView.as_view(), name='register'),
    path('auth/signin', AccountSignInView.as_view(), name='signin'),
    path('auth/signout', AccountSignOutView.as_view(), name='signout'),
    path('<str:account_id>', AccountsUserView.as_view(), name='account'),
    path('<str:account_id>/password',
         ChangePasswordView.as_view(), name='password'),
    path('<str:account_id>/email', ChangeEmailView.as_view(), name='email'),
]

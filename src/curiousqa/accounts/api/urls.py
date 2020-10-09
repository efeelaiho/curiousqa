from accounts.api.views import (AccountRegisterView, AccountSignInView,
                                AccountSignOutView, AccountsUserView)
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('auth/register', AccountRegisterView.as_view(), name='register'),
    path('auth/signin', AccountSignInView.as_view(), name='signin'),
    path('auth/signout', AccountSignOutView.as_view(), name='signout'),
    path('', AccountsUserView.as_view(), name='account'),
]

from accounts.api.user.views import (AccountUserView, ChangeEmailView,
                                     ChangePasswordView)
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('me', AccountUserView.as_view(), name='account'),
    path('me/password', ChangePasswordView.as_view(), name='password'),
    path('me/email', ChangeEmailView.as_view(), name='email'),
]
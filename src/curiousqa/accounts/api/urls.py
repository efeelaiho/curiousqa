from accounts.api.views import AccountRegisterView, AccountsUserView, AccountSignInView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('auth/register', AccountRegisterView.as_view(), name='register'),
    path('auth/signin', AccountSignInView.as_view(), name='signin'),
    path('', AccountsUserView.as_view(), name='account'),
]


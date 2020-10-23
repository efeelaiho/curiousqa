from accounts.api.auth.views import (AccountRegisterView, AccountSignInView,
                                AccountSignOutView)

from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('register', AccountRegisterView.as_view(), name='register'),
    path('signin', AccountSignInView.as_view(), name='signin'),
    path('signout', AccountSignOutView.as_view(), name='signout'),
]
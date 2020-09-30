from accounts.api.views import AccountLoginView, AccountRegisterView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('register', AccountRegisterView.as_view(), name='register')
]


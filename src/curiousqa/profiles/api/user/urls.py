from profiles.api.user.views import ProfileUserView
from django.urls import path

app_name = 'profiles'

urlpatterns = [
    path('me', ProfileUserView.as_view(), name='profile'),
]
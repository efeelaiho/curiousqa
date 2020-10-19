from django.urls import path
from profiles.api.views import ProfileView, ProfilePublicView

app_name = 'profiles'

urlpatterns = [
    path('me', ProfileView.as_view(), name='profile_me'),
    path('<str:profile_id>', ProfileView.as_view(), name='profile_w_id'), 
    path('<str:username>', ProfilePublicView.as_view(), name='public_profile'),   
]
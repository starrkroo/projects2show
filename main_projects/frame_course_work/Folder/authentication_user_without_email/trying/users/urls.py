from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('logout', logout_user, name='logout'),
    path('users/<str:username>/', show_user_profile, name='userprofile')
]

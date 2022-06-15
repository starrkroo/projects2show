from django.urls import path, re_path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('users/<str:username>/', show_user_profile, name='userprofile'),
    path('rooms/id<int:room_id>/', room, name='room'),
    path('checkview/', checkview, name='checkview'),
    path('send', send, name='send'),
    path('getMessages/id<int:room_id>/', getMessages, name='getMessages'),
]

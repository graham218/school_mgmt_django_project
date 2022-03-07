from django.urls import path
from . import views

app_name='base'

urlpatterns = [
    path('lobby/', views.lobby, name='lobby'),
    path('room/', views.room, name='room'),
    path('get_token/', views.getToken, name='get_token'),

    path('create_member/', views.createMember, name='create_member'),
    path('get_member/', views.getMember, name='get_member'),
    path('delete_member/', views.deleteMember, name='delete_member'),
]
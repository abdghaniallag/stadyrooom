 
from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.getHome,name='home'),
    path('room/<str:pk>',views.getRoom,name='room'),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<str:pk>',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>',views.deleteRoom,name='delete-room'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('register',views.registerUser,name='register'),
]

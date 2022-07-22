 
from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.getHome,name='home'),
    path('Room',views.getRoom,name='room'),
]

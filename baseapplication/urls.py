 
from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.getHome,name='home'),
    path('room/',views.getRoom,name='room'),
]

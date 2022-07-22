from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def getHome(request):
    return HttpResponse('home page')

def getRoom(request):
    return HttpResponse('Room page')
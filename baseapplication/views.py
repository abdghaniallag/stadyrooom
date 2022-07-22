from django.shortcuts import render  

def getHome(request):
    return render(request, 'home.html')

def getRoom(request):
    return render(request,'room.html')
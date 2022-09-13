from django.shortcuts import render, redirect
from .models import Room
from .form import RoomForm


def getHome(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    if (request.method == 'POST'):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('invalid form')


    context = {'form': form}
    return render(request, 'base/room_form.html', context)

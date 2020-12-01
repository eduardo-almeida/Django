from django.shortcuts import render
from django.http import HttpResponse


def Ola(request):
    return HttpResponse("Ola Mundo")

def tasklist(request):
    return render(request, 'tasks/list.html') 

def seunome(request, name):
    return render(request, 'tasks/seunome.html', {'nome':name}) 

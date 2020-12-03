from django.shortcuts import render
from django.http import HttpResponse

def dados(request):
    return render(request, 'dadosVisitante/dados.html')
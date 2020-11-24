from django.shortcuts import render
import datetime

def home (request):
    data = {}
    data['agora'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)

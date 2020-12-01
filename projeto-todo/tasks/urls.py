from django.urls import path
from . import views

urlpatterns = [
    path('ola/', views.Ola),
    path('', views.tasklist, name='task-list'),
    path('seunome/<str:name>', views.seunome),
]
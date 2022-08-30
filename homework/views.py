from django.shortcuts import render, HttpResponse
from .models import ToMeet


def page(request):
    return render (request, 'homework.html')

def meeting(request):
    tomeet_list = ToMeet.objects.all()
    return render (request, 'meeting.html', {'tomeet_list':tomeet_list})

def text(request):
    return HttpResponse ('Добро пожаловать в приложение ToDo - Admin) ')
from django.shortcuts import render, HttpResponse
from .models import ToMeet, Goal_for_month


def page(request):
    return render (request, 'homework.html')

def meeting(request):
    tomeet_list = ToMeet.objects.all()
    return render (request, 'meeting.html', {'tomeet_list':tomeet_list})

def text(request):
    return HttpResponse ('Добро пожаловать в приложение ToDo - Admin) ')

def goal(request):
    goals_list=Goal_for_month.objects.all()
    return render (request, 'goals.html', {'goals_list': goals_list})
    
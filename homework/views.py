from django.shortcuts import render, HttpResponse,redirect
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

def add_list(request):
    form = request.POST
    person = form['add_name']
    tomeet = ToMeet(person = person)
    phone_number = form['add_phone']
    tomeet = ToMeet(phone_number = phone_number)
    comment = form['add_comment']
    tomeet = ToMeet(comment=comment)
    date_of_meeting = form ['add_date']
    tomeet = ToMeet(date_of_meeting = date_of_meeting)
    tomeet.save()
    return redirect(meeting)


    
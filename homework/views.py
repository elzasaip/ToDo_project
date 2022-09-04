from django.shortcuts import render, HttpResponse,redirect
from .models import ToMeet, Goal_for_month, Habits


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
    namePerson = form['add_name']
    numPhone = form['add_phone']
    comment = form['add_comment']
    meetingDate = form ['add_date']
    tomeet = ToMeet(person=namePerson, phone_number=numPhone, 
                    comment=comment,date_of_meeting=meetingDate)
    tomeet.save()
    return redirect(meeting)

def habits(request):
    habits_list = Habits.objects.all()
    return render (request,'habits.html',{'habits_list':habits_list})


    
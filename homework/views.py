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

def delete_to_meet(request,id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.delete()
    return redirect(meeting)

def mark_to_meet(request,id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = True 
    tomeet.save()
    return redirect(meeting)

def unmark_to_meet(request,id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = False
    tomeet.save()
    return redirect(meeting)

def close_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_closed = not tomeet.is_closed
    tomeet.save()
    return redirect(meeting)

def add_goals (request):
    form = request.POST
    add_goal = form['add_goal']
    add_month = form['add_month']
    category = form['category']
    add_reason = form['add_reason']
    goals = Goal_for_month(goal=add_goal, month=add_month, difficulty=category, reason_for_goal=add_reason)
    goals.save()
    return redirect(goal)

def delete_goal (request, id):
    goals = Goal_for_month.objects.get(id=id)
    goals.delete()
    return redirect(goal)

def mark_goal (request,id):
    goals = Goal_for_month.objects.get(id=id)
    goals.is_favorite=True
    goals.save()
    return redirect(goal)

def unmark_goal(request, id):
    goals = Goal_for_month.objects.get(id=id)
    goals.is_favorite=False
    goals.save()
    return redirect(goal)

def close_goal(request,id):
    goals = Goal_for_month.objects.get(id=id)
    goals.is_closed = not goals.is_closed
    goals.save()
    return redirect(goal)





    
from django.shortcuts import render, HttpResponse

# Create your views here.


def page(request):
    return render (request, 'homework.html')

def text(request):
    return HttpResponse ('Добро пожаловать в приложение ToDo - Admin) ')
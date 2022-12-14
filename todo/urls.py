"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from homework.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homepage,name="home"),
    path("test/", test, name='test'),
    path('homework/',page, name='homework'),
    path('main/',text,name='message'),
    path('meeting/', meeting, name='meeting'),
    path('goal/',goal, name='goal'),
    path('add-todo/', add_todo,name='add-todo'),
    path('add-list/', add_list, name='add-list'),
    path('habits/', habits, name='habits'),
    path('delete-todo/<id>/', delete_todo, name='delete-todo'),
    path('mark-todo/<id>/', mark_todo, name='mark-todo'),
    path('unmark-todo/<id>/', unmark_todo, name='unmark-todo'),
    path('close-todo/<id>/', close_todo, name='close-todo'),
    path('delete-tomeet/<id>/',delete_to_meet, name='delete-tomeet'),
    path('mark-tomeet/<id>/', mark_to_meet, name='mark-tomeet'),
    path('unmark-tomeet/<id>/',unmark_to_meet, name='unmark-tomeet'),
    path('close-tomeet/<id>/', close_tomeet, name='close-tomeet'),
    path('add-goals/', add_goals, name = 'add-goals'),
    path('delete-goal/<id>/', delete_goal, name='delete-goal'),
    path('mark-goal/<id>', mark_goal, name='mark-goal'),
    path('unmark-goal/<id>', unmark_goal, name='unmark-goal'),
    path('close-goal/<id>', close_goal, name='close-goal'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

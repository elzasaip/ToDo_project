from django.db import models

class ToMeet (models.Model):
    person = models.CharField (max_length=50)
    phone_number = models.CharField (max_length=16)
    date_of_meeting = models.DateField ()
    comment = models.TextField()
    is_closed = models.BooleanField(default = False)
    is_favorite = models.BooleanField(default = False)


class Goal_for_month (models.Model):
    goal = models.CharField(max_length=120)
    month = models.FloatField()
    difficulty = models.BooleanField(default = False)
    reason_for_goal=models.TextField()

class Habits(models.Model):
    name = models.CharField(max_length=50)
    done_for_today = models.BooleanField(default = False)
    important= models.BooleanField(default = False)
    comment = models.TextField()



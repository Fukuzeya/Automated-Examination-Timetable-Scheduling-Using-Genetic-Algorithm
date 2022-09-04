from django.db import models
from django.forms import CharField
from Database.models import  Invigilator


rooms = (
    ('LAB1','LAB1'),('WKSHOP','WKSHOP'),('LAB2','LAB2')
)
class TimeTable(models.Model):
    slot = models.CharField(max_length=10)
    program = CharField(max_length=100)
    module = models.CharField(max_length=25)
    title = models.CharField(max_length=100, null=True)
    students= models.IntegerField()
    room = models.CharField(max_length=100, null=True,choices=rooms)
    date = models.CharField(max_length=25)
    time = models.CharField(max_length=25)
    has_assigned = models.BooleanField(default=False)

    @property
    def invigilator(self):
        return self.slot_invigilator.all()[0].invigilator.name 
        
    def __str__(self):
        return f'{self.module} [{self.date} : {self.time}]'

class Scheduling(models.Model):
    session_start = models.DateField()
    session_end = models.DateField()

class DoneScheduling(models.Model):
    has_done = models.BooleanField(default=True)

class InvigilatorAssignment(models.Model):
    slot = models.ForeignKey(TimeTable,on_delete=models.CASCADE,related_name='slot_invigilator',null=True,blank=True)
    invigilator = models.ForeignKey(Invigilator, on_delete=models.DO_NOTHING, related_name='allocated_dates',null=True,blank=True)


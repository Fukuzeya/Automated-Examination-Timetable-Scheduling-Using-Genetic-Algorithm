from django.shortcuts import render
from .models import *
# Create your views here.

def get_data():
    #get faculties
    FACULTIES = Faculty.objects.all()
    #get departments
    DEPARTMENTS = Department.objects.all()
    #get programmes
    PROGRAMS = Program.objects.filter(is_available = True)
    #get modules
    MODULES = Module.objects.filter(borrowed = False)
    #get exam sessions
    SESSIONS = Session1.objects.all()
    #get exam rooms
    ROOMS = Room.objects.filter(is_available = True)
    #get invigilators
    INVIGILATORS = Invigilator.objects.filter(is_available = True)
    data = {
        'FACULTIES':FACULTIES,
        'DEPARTMENTS':DEPARTMENTS,
        'PROGRAMS':PROGRAMS,
        'MODULES':MODULES,
        'SESSIONS':SESSIONS,
        'INVIGILATORS':INVIGILATORS,
        'ROOMS':ROOMS
        }
    return data

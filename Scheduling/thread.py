import threading
from django.http import JsonResponse
from django.shortcuts import render,redirect
import random as rnd
import datetime
from Algorithm.prettytable import PrettyTable
from Database.models import *
from Algorithm.scheduling import *
from .models import TimeTable,DoneScheduling

class ExamSchedulingThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        displayMgr = DisplayMgr()
        displayMgr.print_available_data()
        generationNumber =0
        print('\n> Generation # ' + str(generationNumber))
        population = Population(POPULATION_SIZE)
        population.get_schedules().sort(key=lambda x:x.get_fitness(),reverse=True)
        displayMgr.print_generation(population)
        displayMgr.print_schedule_as_table(population.get_schedules()[0])

        geneticAlgorithm = GeneticAlgorithm()
        while((population.get_schedules()[0].get_fitness() !=1.0) or generationNumber == 50):
            generationNumber +=1
            
            print("\n> Generation #" + str(generationNumber))
            population = geneticAlgorithm.evolve(population)
            population.get_schedules().sort(key=lambda x:x.calculate_fitness(),reverse=True)
            displayMgr.print_generation(population)
            displayMgr.print_schedule_as_table(population.get_schedules()[0])
            if generationNumber == 220:
                return
        print("\n\n")
        print('********************Algorithm done scheduling******************')
        #displayMgr.print_schedule_as_table(population.get_schedules()[0])

        #===============================
        print('********************Populating Database******************')
        schedule = population.get_schedules()[0]
        slots = schedule.get_slots()
        #clear timetable 
        TimeTable.objects.all().delete()
        for i in range(0,len(slots)):
            timetable = TimeTable()
            timetable.slot = str(i)
            timetable.program= slots[i].get_programs().get_program_code()
            timetable.module =slots[i].get_modules().get_module_code()
            timetable.title =slots[i].get_modules().get_title()
            timetable.students =slots[i].get_modules().get_numOfStudents()
            timetable.room =slots[i]. get_room().get_room_number()
            timetable.date =slots[i].get_session().get_date()
            timetable.time = slots[i].get_session().get_time()
            timetable.save()
            
        DoneScheduling.objects.create()
        print('********************ALL DONE******************')

        return JsonResponse({'id':'done'})
        # return redirect('admin:index')

        print('********************ERROR OCCURED ON BACKGROUND THREAD******************')
                    
        
            







        #     try:
        #     displayMgr = DisplayMgr()
        #     displayMgr.print_available_data()
        #     generationNumber =0
        #     print('\n> Generation # ' + str(generationNumber))
        #     population = Population(POPULATION_SIZE)
        #     population.get_schedules().sort(key=lambda x:x.get_fitness(),reverse=True)
        #     displayMgr.print_generation(population)
        #     displayMgr.print_schedule_as_table(population.get_schedules()[0])

        #     geneticAlgorithm = GeneticAlgorithm()
        #     while((population.get_schedules()[0].get_fitness() !=1.0) or generationNumber == 50):
        #         generationNumber +=1
        #         print("\n> Generation #" + str(generationNumber))
        #         population = geneticAlgorithm.evolve(population)
        #         population.get_schedules().sort(key=lambda x:x.calculate_fitness(),reverse=True)
        #         displayMgr.print_generation(population)
        #         displayMgr.print_schedule_as_table(population.get_schedules()[0])
        #     print("\n\n")
        #     print('********************Algorithm done scheduling******************')
        #     #displayMgr.print_schedule_as_table(population.get_schedules()[0])

        #     #===============================
        #     print('********************Populating Database******************')
        #     schedule = population.get_schedules()[0]
        #     slots = schedule.get_slots()
        #     #clear timetable 
        #     TimeTable.objects.all().delete()
        #     for i in range(0,len(slots)):
        #         timetable = TimeTable()
        #         timetable.slot = str(i)
        #         timetable.program=slots[i].get_programs().get_program_code()
        #         timetable.module =slots[i].get_modules().get_module_code()
        #         timetable.students =slots[i].get_modules().get_numOfStudents()
        #         timetable.room =slots[i]. get_room().get_room_number()
        #         timetable.date =slots[i].get_session().get_date()
        #         timetable.time = slots[i].get_session().get_time()
        #         timetable.save()
        #     print('********************ALL DONE******************')

        #     return redirect('admin:index')
        # except Exception as e:
        #     print('********************ERROR OCCURED ON BACKGROUND THREAD******************')
        #     print(e)
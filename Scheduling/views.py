import re
import datetime

from django.http import JsonResponse
from django.db.models import Count
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

from Algorithm.scheduling import *
from Database.models import *
from .models import TimeTable, DoneScheduling
from .forms import SessionForm
from .thread import ExamSchedulingThread
from .create_table_fpdf2 import PDF


#validate examination period
# minimum date should be 5 days
def is_valid_date_range(start,end):
    if (end - start).days <5:
        return False
    return True

#validate examination period
# maximum date should be 12 days
def is_valid_date_range2(start,end):
    if (end - start).days > 12:
        return False
    return True

# define sessions excluding weekends from start date 
# to end date
def workdays(d, end, excluded=(6, 7)):
    days = []
    while d <= end:
        if d.isoweekday() not in excluded:
            days.append(d)
        d += datetime.timedelta(days=1)
    for day in days:
        counter = 1
        session = "S"+ str(counter) + " AM"
        # add session to the database
        session_obj = Session(session_id = session,date=day,time = "[09:00-12:00]")
        session_obj.create()

        session = "S"+ str(counter) + " PM"
        # add session to the database
        session_obj2 = Session(session_id = session,date=day,time = "[14:00-17:00]")
        session_obj2.create()

#add session view
def add_session(request):
    if request.method =='POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if not is_valid_date_range(start_date, end_date):
                messages.error(request,"Examination period should not be less than 5 days.")
                return HttpResponseRedirect(reverse('scheduling:exam_session'))

            if not is_valid_date_range2(start_date, end_date):
                messages.error(request,"Examination period should not exceed two weeks.")
                return HttpResponseRedirect(reverse('scheduling:exam_session'))
            excluded=(6, 7)
            counter = 1
            days = []
            while start_date <= end_date:
                if start_date.isoweekday() not in excluded:
                    days.append(start_date)
                start_date += datetime.timedelta(days=1)
            #clear the session table 
            # so as to enter new sessions
            Session1.objects.all().delete()
            #delete value that indicates that the timetable is done scheduled
            DoneScheduling.objects.all().delete()
            for day in days:
                session = "S"+ str(counter) + " AM"
                print(f'{day} S1 [09:00-12:00]AM')
                # add session to the database
                Session1.objects.create(session_id = session,date=day,time = "[09:00-12:00]")
                session = "S"+ str(counter) + " PM"
                # add session to the database
                Session1.objects.create(session_id = session,date=day,time = "[14:00-17:00]")
                counter +=1

            return redirect('scheduling:simulation')
    else:
        form = SessionForm()
    return render(request,'exam/scheduling.html',{'form':form})

#start examination scheduling
def simulate_scheduling(request):
    #start the thread which run the algorithm
    ExamSchedulingThread().start()
    return render(request, 'simulation.html')

#check if the timetable done scheduled using jquery
def has_scheduling(request):
    counts = DoneScheduling.objects.all().count()
    if counts == 1:
        return JsonResponse({'id':True})
    else:
        return JsonResponse({'id':False})
        
def get_timetable(request):
    timetables = TimeTable.objects.values('date','module','title','students','room','time').annotate(Count('date')).order_by('date','time') # ensure you add the order_by()
    return render(request,'exam/timetable.html',{'timetables':timetables})

def get_timetable_pdf(request):
    timetables = TimeTable.objects.values('date','module','title','students','room','time').annotate(Count('date')).order_by('date','time') # ensure you add the order_by()
    data = [
        ["Date", "Module", "Title", "Students","Venue","Time",]]
    for slot in timetables:
        data.append([str(slot['date']),slot['module'],slot['title'],str(slot['students']),slot['room'],slot['time'],])

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=10)
    tit = f"MSUAS\nFINAL EXAMINATION TIMETABLE."
    pdf.create_table(table_data = data,title=tit, cell_width='even')
    pdf.ln()
    pdf.output('exam_timetable.pdf')
    return redirect('scheduling:get_timetable')

'''
the function is used to reschedule module timetable
and several constraints needs to be checked
1.check if the entered module code is valid
2.check if module code exist
3.check if the selected room has free seats to accomodate given students
4.check if there is no clash with already allocated module for that day and time
belong to the same program and level

'''
levels = ['1.1','1.2','2.1','2.2','3.1','3.2','4.1','4.2','5.1','5.2']

def reschedule_exams(request):
    sessions = Session1.objects.all()
    search_rooms = Room.objects.filter(is_available=True)
    programs = Program.objects.filter(is_available = True)
    if request.method =='POST':
        module_code = request.POST['module_code']
        students = request.POST['students']
        session_id = request.POST['session']
        room_id = request.POST['room']

        #validate module
        student_id_format = re.compile(r"^[A-Z]{3,6}\d{3}$")
        pattern = student_id_format.search(module_code)
        if not pattern:
            messages.error(request,"Invalid module code format")
            return HttpResponseRedirect(reverse('scheduling:exam_reschedule'))
        
        if not Module.objects.filter(module_code = module_code).exists():
            messages.error(request,"Module does not exist in our database.")
            return HttpResponseRedirect(reverse('scheduling:exam_reschedule'))
        
        #get module
        module = Module.objects.get(module_code = module_code, borrowed = False)
        session = Session1.objects.get(id = session_id)
        room = Room.objects.get(id = room_id)
        timetable = TimeTable.objects.filter(date = str(session.date),time = session.time, room = room.room_number)
        #get total number of students
        total_students = 0
        for slot in timetable:
            total_students += int(slot.students)
        #validate room seats
        if (int(room.seating_capacity) - total_students) < int(students):
            messages.error(request,"Available " + str(int(room.seating_capacity) - total_students) + " seats can not accomodate " + str(students) +" students specified.")
            return HttpResponseRedirect(reverse('scheduling:exam_reschedule'))

        #check if there are no related modules assigned for that day
        day_slots = TimeTable.objects.filter(date = str(session.date))
        related_modules = Module.objects.filter(programme_code = module.programme_code, level = module.level)
        module_codes = []
        for modul in related_modules:
            module_codes.append(modul.module_code)

        for day_slot in day_slots:
            if day_slot.module in module_codes:
                messages.error(request,"Reschedule failed!, module clashed with " + day_slot.title)
                return HttpResponseRedirect(reverse('scheduling:exam_reschedule'))
        
        # check if the module was already scheduled
        #if so delete the schedule of the module
        if TimeTable.objects.filter(module = module.module_code).exists():
            TimeTable.objects.get(module = module.module_code).delete()
            TimeTable.objects.create(
                slot = "reschedule",
                module = module.module_code,
                title = module.title,
                students = students,
                room = room.room_number,
                date = session.date,
                time = session.time

            )
            messages.success(request,"Module rescheduled successful")
            return HttpResponseRedirect(reverse('scheduling:exam_reschedule'))
        

    return render(request,'exam/reschedule.html',{'sessions':sessions,'rooms':search_rooms})

'''
a report of exam room allocations indicates the number 
of students allocated to each venue on each session
and the available seats 
'''
#Get timetable report
def get_timetable_report(request):
    sessions = Session1.objects.all()
    timetable = TimeTable.objects.all()
    rooms = Room.objects.filter(is_available = True)
    room_reports = []
    #for each room get report of students allocated
    for room in rooms:
        day_session = []
        for session in sessions:
            students = 0
            for slot in timetable:
                if (slot.room == room.room_number) and str(slot.date) == str(session.date) and slot.time == session.time:
                    students = students + int(slot.students)
            day_session.append([session,students])
        room_reports.append([room,day_session])

    return render(request, 'exam/timetable-report.html',{'reports':room_reports})

from datetime import datetime
import io
from django.shortcuts import redirect, render
from django.http import FileResponse, HttpResponse

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from Database.models import *
from Scheduling.models import InvigilatorAssignment, TimeTable
from Accounts.models import *
from .create_table_fpdf2 import PDF

#homepage
def home_page(request):
    return render(request, 'index.html')

#get all departments
def get_all_departments(request):
    departments = Department.objects.all()
    return render(request, 'exam/departments.html',{'departments':departments})

#get all modules
def get_all_programmes(request):
    programmes = Program.objects.all()
    return render(request, 'exam/programs.html',{'programmes':programmes})

#get all modules
def get_all_modules(request):
    modules = Module.objects.all().exclude(borrowed=True)
    return render(request, 'exam/modules.html',{'modules':modules})

#get all exam rooms
def get_all_exam_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'exam/exam-rooms.html',{'rooms':rooms})

#get all invigilators
def get_all_invigilators(request):
    invigilators = Invigilator.objects.all()
    return render(request, 'exam/invigilators.html',{'invigilators':invigilators})

#get all modules
def get_registration_information(request):
    registrations = Registration.objects.all().order_by('-no_of_students')
    return render(request, 'exam/registration.html',{'registrations':registrations})

def get_department_timetable(request):
    hod = Hod.objects.get(ec_number = request.user.username)
    department = Department.objects.get(id=hod.id)
    #get programs for the department
    programes = department.department_programs.all()
    #get modules for the department
    department_modules = department.department_modules.all()

    timetable = TimeTable.objects.all()
    department_timetable = []
    '''
    select all the slots with modules in timetable
    which are also in the department modules

    '''
    for module in department_modules:
        for slot in timetable:
            if module.module_code == slot.module:
                department_timetable.append(slot)
    return render(request,'hod/timetable.html',{'timetables':department_timetable,'programes':programes,'department':department})

def get_department_timetable_pdf(request):
    hod = Hod.objects.get(ec_number = request.user.username)
    department = Department.objects.get(id=hod.id)
    department_modules = department.department_modules.all()
    timetable = TimeTable.objects.all()
    department_timetable = []
    for module in department_modules:
        for slot in timetable:
            if module.module_code == slot.module:
                department_timetable.append(slot)

    '''
    generate the pdf of the selected department timetable
    '''
    data = [
        ["Date", "Module", "Title", "Students","Venue","Time",]]
    for slot in department_timetable:
        data.append([str(slot.date),slot.module,slot.title,str(slot.students),slot.room,slot.time,])

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=10)
    tit = f"MSUAS\nDEPARTMENT OF {department.department_name} TIMETABLE."
    pdf.create_table(table_data = data,title=tit, cell_width='even')
    pdf.ln()
    pdf.output('department_timetable.pdf')
    return redirect('management:department_timetable')

def get_program_timetable(request,id):
    program = Program.objects.get(id=id)
    program_modules = program.program_modules.all()
    timetable = TimeTable.objects.all()
    program_timetable = []
    for module in program_modules:
        for slot in timetable:
            if module.module_code == slot.module:
                program_timetable.append(slot)

    # timetables = department_timetable.values('date','module','title','students','room','time').annotate(Count('date')).order_by('date','time') # ensure you add the order_by() 
    return render(request,'hod/timetable.html',{'timetables':program_timetable,'program':program.programme_name})

def student_profile(request):
    student = Student.objects.get(reg_number= request.user.username)
    modules = student.registered_students.all()
    print(modules)
    return render(request, "student/profile.html",{'student':student,'modules':modules})

def student_modules(request):
    student = Student.objects.get(reg_number= request.user.username)
    modules = student.registered_students.all()
    print(modules)
    return render(request, "student/modules.html",{'modules':modules})

def get_student_time_table(request):
    student = Student.objects.get(reg_number = request.user.username)
    student_modules = student.registered_students.all()
    my_modules = []
    for registration in student_modules:
        module = registration.module
        my_modules.append(module)

    timetable = TimeTable.objects.all()
    student_timetable = []
    for module in my_modules:
        for slot in timetable:
            if module.module_code == slot.module:
                student_timetable.append(slot)

    # timetables = department_timetable.values('date','module','title','students','room','time').annotate(Count('date')).order_by('date','time') # ensure you add the order_by() 
    return render(request,'student/timetable.html',{'timetables':student_timetable})

def get_student_time_table_pdf(request):
    student = Student.objects.get(reg_number = request.user.username)
    student_modules = student.registered_students.all()
    my_modules = []
    for registration in student_modules:
        module = registration.module
        my_modules.append(module)

    timetable = TimeTable.objects.all()
    student_timetable = []
    for module in my_modules:
        for slot in timetable:
            if module.module_code == slot.module:
                student_timetable.append(slot)
    
    data = [
        ["Date", "Module", "Title", "Students","Venue","Time",]]
    for slot in student_timetable:
        data.append([str(slot.date),slot.module,slot.title,str(slot.students),slot.room,slot.time,])

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=10)
    tit = f"MSUAS\n{student.programme_code.programme_name} Level {student.level} TIMETABLE."
    pdf.create_table(table_data = data,title=tit, cell_width='even')
    pdf.ln()
    pdf.output('personal_timetable.pdf')
    return redirect('management:student_timetable')

def signup(request):
    return render(request, 'accounts/signup.html')

#generate timetable
def generate_module_pdf(request):
    #Create ByteStream Buffer
    buf = io.BytesIO()
    #create canvas
    c = canvas.Canvas(buf, pagesize=letter,bottomup=0)
    #create object
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
    #add some lines of text
    lines = [
        "MODULE CODE\t\tTITLE",
    ]
    student = Student.objects.get(reg_number= request.user.username)
    modules = student.registered_students.all()
    for module in modules:
        lines.append(f"{module.module.module_code}\t\t{module.module.title}")
        lines.append(" ")
    #loop through the lines

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="registered_modules.pdf")

#generate pdf
def export_pdf(request):
    response = HttpResponse(content_type ='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=timetable' + \
     str(datetime.datetime.now()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

#assign invigilators
def assign_invigilators(request):
    invigilators = Invigilator.objects.all()
    number_of_invigilators =Invigilator.objects.all().count()
    timetable = TimeTable.objects.all()
    count =0
    for slot in timetable:
        while(slot.has_assigned == False):
            if count == number_of_invigilators:
                count = 0
            invigilator =invigilators[count]
            module = Module.objects.get(module_code = slot.module,borrowed = False)
            if not (module.department_code == invigilator.department.department_code):
                InvigilatorAssignment.objects.create(slot =slot, invigilator=invigilator)
                slot.has_assigned =True
                slot.save()
            count +=1
        
    return redirect('scheduling:get_timetable')


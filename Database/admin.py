from django.contrib import admin
from django import forms
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
from .models import *


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_code','faculty_name','is_available')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_code','department_name','faculty_code','is_available')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('programme_code','programme_name','department_code','is_available')

class SharedProgramInline(admin.TabularInline):
    model = SharedPrograms
    extra =5

@admin.register(Module)
class ModuleAdmin(ImportExportModelAdmin):
    list_display = ('module_code','title','level','programme_code','numOfStudents','isMassModule','is_available')
    search_fields =('module_code',)
    inlines =[SharedProgramInline]
    
@admin.register(Student)
class Studentdmin(ImportExportModelAdmin):
    list_display = ('reg_number','surname','firstname','gender','programme_code','level','is_registered')
    actions = ('registration',)
    #register modules
    def registration(self,request,queryset):
        for student in queryset:
            if not student.is_registered:
                #get program
                _program = Program.objects.get(id = student.programme_code.id)
                #get modules
                modules = _program.program_modules.filter(level= student.level)
                for module in modules:
                    reg_module = Registration.objects.get(module= module)
                    reg_module.no_of_students += 1
                    reg_module.students.add(student)
                    reg_module.save()
                    student.is_registered = True
                    student.save()


class InvigilatorForm(forms.ModelForm):
    def clean(self):
        ec_number = self.cleaned_data['ec_number']
        if not ec_number.istitle():
            raise forms.ValidationError({'ec_number': "Not a proper titlecased string"})

# @admin.register(Invigilator)
# class InvigilatorAdmin(SummernoteModelAdmin):
#     form = InvigilatorForm
#     list_display = ('department','name','ec_number','is_available')

@admin.register(Invigilator)
class InvigilatorAdmin(admin.ModelAdmin):
    form = InvigilatorForm
    list_display = ('department','name','ec_number','is_available')

@admin.register(Registration)
class Registrationdmin(admin.ModelAdmin):
    list_display = ('module','no_of_students')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number','seating_capacity','venue')
    #list_filter =['program','room','date','time']

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_id','date','time')

@admin.register(Session1)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_id','date','time')







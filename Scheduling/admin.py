from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django import forms

from .models import *

admin.site.site_header ='MSUAS EXAM DEPTMENT'
admin.site.site_title ='MSUAS | Exam'
admin.site.index_title ='Examination Timetable'

# Register your models here.

class TimetableForm(forms.ModelForm):
    def clean(self):
        module = self.cleaned_data['module']
        title = self.cleaned_data['title']
        students = self.cleaned_data['students']
        room = self.cleaned_data['room']
        date = self.cleaned_data['date']
        time = self.cleaned_data['time']

        if TimeTable.objects.filter(module = module).exists():
            raise forms.ValidationError({'module': "Module already exists"})

        if not module.istitle():
            raise forms.ValidationError({'module': "Not a proper titlecased string"})
        if not title.istitle():
            raise forms.ValidationError({'title': "Not a proper titlecased string"})

@admin.register(TimeTable)
class TimeTableAdmin(SummernoteModelAdmin):
    form = TimetableForm
    list_display = ('module','title','students','room','date','time','invigilator')
    list_filter =['module','room','date','time']
    search_fields =('module',)
    actions = ('unassign',)

    #un assign invigilators
    def unassign(self,request,queryset):
        for slot in queryset:
            slot.has_assigned =False
            slot.save()

@admin.register(DoneScheduling)
class DoneAdmin(SummernoteModelAdmin):
    pass

@admin.register(InvigilatorAssignment)
class InviAdmin(SummernoteModelAdmin):
    pass

from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from datetime import date

from Database.datastructures import Program
from Database.models import Session

#add session form
class SessionForm(forms.ModelForm):
    start_date= forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Session
        fields =['start_date','end_date']
    
    #validate exam start date
    def clean_start_date(self):
        start_date= self.cleaned_data['start_date'] 
        excluded=(6, 7)
        if start_date.isoweekday() in excluded:
            raise ValidationError('Exams cannot start on weekend!')
        to_date = date.today()
        diff = start_date - to_date
        diff_days =diff.days
        if diff_days < 5:
            raise ValidationError('Timetable must be scheduled 5 days ahead.')
        return start_date

    #validate exam end date
    def clean_end_date(self):
        end_date= self.cleaned_data['end_date'] 
        excluded=(6, 7)
        if end_date.isoweekday() in excluded:
            raise ValidationError('Exams cannot end on weekend!')
        to_date = date.today()
        diff = end_date - to_date
        diff_days =diff.days
        # if diff_days < 5:
        #     raise ValidationError('Examination time frame must be atleaset 5 days.')
        return end_date

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update(
            {'class': 'form-control'})


from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

import re

from Database.models import Student
from .models import Codes, Staff,Hod

#forms
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control signup-name','Label':'Username:','Placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control signin-password',
            'id': 'password',
            'Placeholder':'Your password'
        }
    ))

class StaffSignUp(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name','password1','password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        applicant = Staff.objects.filter(ec_number = username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        if not applicant.count():
            raise forms.ValidationError("Your EC Number is not recognised!")
        return username

    def clean_first_name(self):
        phone_number = self.cleaned_data['first_name']
        mobile_number_format = re.compile(r"^[7]\d{8}$")
        pattern = mobile_number_format.search(str(phone_number))
        if not pattern:
            raise ValidationError('Invalid Mobile Number!')
        return phone_number

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control signup-name','placeholder':'Enter EC Number'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control signup-number','placeholder':'Enter Phone Number'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control signup-password','placeholder':'Enter Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control signup-password','placeholder':'Confirm Password'})

class CodeForm(forms.ModelForm):
    code = forms.CharField(max_length=5)

    class Meta:
        model = Codes
        fields = ('code',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].widget.attrs.update(
            {'class': 'form-control signup-name','placeholder':'Enter the code.'})

class HodSignUp(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name','password1','password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        applicant = Hod.objects.filter(ec_number = username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        if not applicant.count():
            raise forms.ValidationError("Your EC Number is not recognised!")
        return username

    def clean_first_name(self):
        phone_number = self.cleaned_data['first_name']
        mobile_number_format = re.compile(r"^07\d{8}$")
        pattern = mobile_number_format.search(str(phone_number))
        if not pattern:
            raise ValidationError('Invalid Mobile Number!')
        return phone_number

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control signup-name','placeholder':'Enter EC Number'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control signup-number','placeholder':'Enter Phone Number'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control signup-password','placeholder':'Enter Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control signup-password','placeholder':'Confirm Password'})

class StudentSignUp(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name','password1','password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        applicant = Student.objects.filter(reg_number = username)
        if r.count():
            raise forms.ValidationError("Reg number already exists")
        if not applicant.count():
            raise forms.ValidationError("Your Student ID is not recognised!")
        return username

    def clean_first_name(self):
        phone_number = self.cleaned_data['first_name']
        mobile_number_format = re.compile(r"^07\d{8}$")
        pattern = mobile_number_format.search(str(phone_number))
        if not pattern:
            raise ValidationError('Invalid Mobile Number!')
        return phone_number

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control signup-name','placeholder':'Enter Student ID'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control signup-number','placeholder':'Enter Phone Number'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control signup-password','placeholder':'Enter Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control signup-password','placeholder':'Confirm Password'})
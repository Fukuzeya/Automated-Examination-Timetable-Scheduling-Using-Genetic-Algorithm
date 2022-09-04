from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import *
from .forms import *
from .utils import send_sms

@login_required
def home(request):
    return render(request, 'home.html')

def is_admin(user):
    return user.groups.filter(name='Admins').exists()
def is_staff(user):
    return user.groups.filter(name='Staff').exists()

def is_hod(user):
    return user.groups.filter(name='hod').exists()

def is_student(user):
    return user.groups.filter(name='Students').exists()

#entry page for every user
def profile_entry(request):
    if is_staff(request.user):
        return redirect('management:get_programmes')
    elif is_hod(request.user):
        return redirect('management:department_timetable')
    elif is_student(request.user):
        return redirect('management:student_prof')
    elif is_admin(request.user):
        return redirect('admin:index')


def register_User(request):
    if request.method =='POST':
        form = StaffSignUp(request.POST)
        username = request.POST.get('username')
        if form.is_valid():
            member = Staff.objects.get(ec_number = username)
            #get the group where the user was assigned
            group  = Group.objects.get(name=member.access_level)
            user = form.save()
            #add user to the group
            group.user_set.add(user)
            return redirect('accounts:login')
    else:
        form = StaffSignUp()
    return render(request,'accounts/signup.html',{'form':form})

def register_Hod(request):
    if request.method =='POST':
        form = HodSignUp(request.POST)
        username = request.POST.get('username')
        if form.is_valid():
            member = Hod.objects.get(ec_number = username)
            group  = Group.objects.get(name="hod")
            user = form.save()
            group.user_set.add(user)
            return redirect('accounts:login')
    else:
        form = HodSignUp()
    return render(request,'accounts/hod-signup.html',{'form':form})

def register_Student(request):
    if request.method =='POST':
        form = StudentSignUp(request.POST)
        if form.is_valid():
            group  = Group.objects.get(name="Students")
            user = form.save()
            group.user_set.add(user)
            return redirect('accounts:student_login')
    else:
        form = StudentSignUp()
    return render(request,'accounts/student-signup.html',{'form':form})

#authenticate user
def auth_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        #if user enters correct credential 
        # redirect the user to the code verification form
        if user is not None:
            request.session['pk'] = user.id
            return redirect('accounts:verify_user')
        else:
            messages.error(request,"Invalid username and or password!")
            return HttpResponseRedirect(reverse('accounts:login'))

    return render(request, 'accounts/login.html',{'form':form})

def hod_auth_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.id
            return redirect('accounts:verify_user')
        else:
            messages.error(request,"Invalid username and or password!")
            return HttpResponseRedirect(reverse('accounts:hod_login'))

    return render(request, 'accounts/hod-login.html',{'form':form})

def student_auth_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.id
            return redirect('accounts:verify_user')
        else:
            messages.error(request,"Invalid username and or password!")
            return HttpResponseRedirect(reverse('accounts:student_login'))

    return render(request, 'accounts/student-login.html',{'form':form})

def verify_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = User.objects.get(pk=pk)
        code = user.user_code
        code_user = f"{user.username}:{user.user_code}"
        if not request.POST:
            print(code_user)
            #send SMS
            #first name represent phone_numner
            #did not want to override user
            number = "+263"+ str(user.first_name)
            send_sms(number,code_user)

        if form.is_valid():
            num = form.cleaned_data.get('code')

            if str(code) == num:
                code.save()
                login(request, user)
                return redirect('accounts:user_profile')
            else:
                messages.error(request,"Invalid authentication code")
                return HttpResponseRedirect(reverse('accounts:verify_user'))
        
    return render(request, 'accounts/codes.html',{'form':form})


import profile
from django.urls import path
from .views import *



app_name = 'accounts'

urlpatterns =[
    path('home/',home, name='home_page'),
    path('users/auth/register/account/',register_User, name='register_account'),
    path('users/hod/auth/register/account/',register_Hod, name='register_hod_account'),
    path('verify/',verify_view, name='verify_user'),
    path('login/', auth_view, name='login'),
    path('hod/login/', hod_auth_view, name='hod_login'),
    path('user/profile/entry/',profile_entry, name='user_profile'),
    path('student/auth/login/', student_auth_view, name="student_login"),
    path('student/auth/signup/',register_Student, name="student_signup"),
    
]
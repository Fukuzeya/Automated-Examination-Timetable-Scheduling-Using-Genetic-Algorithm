from django.urls import path
from .views import *


app_name='management'

urlpatterns =[
    path('', home_page, name="home"),
    path('departments/',get_all_departments, name='get_departments'),
    path('programmes/',get_all_programmes, name='get_programmes'),
    path('modules/',get_all_modules, name='get_modules'),
    path('exam/rooms/',get_all_exam_rooms, name='get_exam_rooms'),
    path('invigilators/',get_all_invigilators, name='get_invigilators'),
    path('registration/',get_registration_information, name='get_registration_info'),
    path('department/timetable/',get_department_timetable, name='department_timetable'),
    path('student/profile/',student_profile, name="student_prof"),
    path('student/timetable/',get_student_time_table, name='student_timetable'),
    path('accounts/auth/signup/',signup, name='account_signup'),
    path('program/timetable/<int:id>/', get_program_timetable, name="program_timetable"),
    path('student/registered/modules/',student_modules, name='student_registered_modules'),
    path('timetable/pdf/',generate_module_pdf,name="module_pdf"),
    path('generate/pdf/',export_pdf, name='get_pdf'),
    path('invigilator/assignment/',assign_invigilators,name='assign_invigilator'),
    path('allocate/seatingposition/',allocate_seating_position,name='seating_position'),
    path('department/timetable/pdf/',get_department_timetable_pdf,name='department_pdf'),
    path('student/timetable/pdf/',get_student_time_table_pdf,name='student_pdf'),
]
from django.urls import path
from .views import *


app_name='scheduling'

urlpatterns =[
    path('status/', has_scheduling, name="scheduling_alg"),
    path('add/session/',add_session, name='exam_session'),
    path('simulation/',simulate_scheduling, name='simulation'),
    path('view/timetable/',get_timetable, name='get_timetable'),
    path('exam/reschedule/',reschedule_exams, name='exam_reschedule'),
    path('rescheduling/',individual_timetable_reschedule, name='reschedule'),
    path('room/allocation/report/',get_timetable_report,name='room_report'),
    path('timetable/pdf',get_timetable_pdf, name='timetable_pdf'),

]
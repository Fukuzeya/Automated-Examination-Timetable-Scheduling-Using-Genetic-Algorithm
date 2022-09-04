from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','ec_number','gender','access_level')

@admin.register(Hod)
class HodAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','ec_number','gender','department')

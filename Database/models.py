from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

levels = (
    ('1.1','1.1'),('1.2','1.2'),('2.1','2.1'),('2.2','2.2'),
    ('3.1','3.1'),('3.2','3.2'),('4.1','4.1'),('4.2','4.2'),
    ('5.1','5.1'),('5.2','5.2')
)

#Faculty Table
class Faculty(models.Model):
    faculty_code = models.CharField(max_length=10, unique=True)
    faculty_name = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.faculty_name

#Department table
class Department(models.Model):
    department_code = models.CharField(max_length=10, unique=True)
    department_name = models.CharField(max_length=50)
    faculty_code = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='faculty_departments')
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.department_name

#Programs table
class Program(models.Model):
    programme_code = models.CharField(max_length=10, unique=True)
    programme_name = models.CharField(max_length=50)
    department_code = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_programs')
    is_available = models.BooleanField(default=True)
    def get_program_code(self):return self.programme_code
    def get_program_name(self):return self.programme_name
    def get_department(self):return self.department_code
    def get_modules(self):
        modules = Module.objects.filter(programme_code = self.id, borrowed = False)
        return modules
    
    #get level modules
    def get_level_1_1_modules(self):
        modules = Module.objects.filter(programme_code = self.id,level='1.1',borrowed=False)
        return modules
    def get_level_1_2_modules(self):
        modules = Module.objects.filter(programme_code = self.id,level='1.2',borrowed=False)
        return modules
    def get_level_2_1_modules(self):
        modules = Module.objects.filter(programme_code = self.id,level='2.1',borrowed=False)
        return modules
    def get_level_2_2_modules(self):
        modules = Module.objects.filter(programme_code = self.id,level='2.2',borrowed=False)
        return modules
    def get_level_3_1_modules(self):
        modules = Module.objects.filter(programme_code = self.id,level='3.1',borrowed=False)
        return modules
    def get_level_3_2_modules(self):
        modules = Module.objects.filter(programme_code = self.id,level='3.2',borrowed=False)
        return modules
    def get_level_4_1_modules(self):
        modules = Module.objects.filter(programme_code = self.id,level='4.1',borrowed=False)
        return modules
    def get_level_4_2_modules(self):
        modules = Module.objects.filter(programme_code = self.id,level='4.2',borrowed=False)
        return modules
    def get_level_5_1_modules(self):
        modules = Module.objects.filter(programme_code = self.id,level='5.1',borrowed=False)
        return modules
    def get_level_5_2_modules(self):
        modules = Module.objects.filter(programme_code = self.id,level='5.2',borrowed=False)
        return modules
    def search_modules(self,level):
        modules = Module.objects.filter(programme_code = self.id,level=level)
        return modules
    def search_modules_without_borrowed(self,level):
        modules = Module.objects.filter(programme_code = self.id,level=level,borrowed=False)
        return modules
        
    def __str__(self): return self.programme_name

#Module table
class Module(models.Model):
    module_code = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    programme_code = models.ForeignKey(Program, on_delete=models.CASCADE, related_name = 'program_modules')
    department_code = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_modules')
    level = models.CharField(max_length=10,choices=levels)
    module_credits = models.IntegerField()
    isMassModule = models.BooleanField(default = False)
    numOfStudents = models.IntegerField(default=0)
    borrowed = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def get_module_code(self):return self.module_code
    def get_title(self):return self.title
    def get_program_code(self):return self.programme_code
    def get_level(self):return self.level
    def get_numOfStudents(self):
        if Registration.objects.filter(module = self).exists():
            module = Registration.objects.get(module = self)
            return  module.no_of_students
        return 0
    def get_isMassModule(self):return self.isMassModule
    def get_shared_programs(self):return self.share_programs.all()
    def get_dept_id(self):return self.department_code

    def __str__(self):return self.module_code

#Module registration
@receiver(post_save, sender=Module)
def default_module_registration(sender,instance,created, **kwargs):
    if created:
        if not Registration.objects.filter(module = instance).exists():
            Registration.objects.create(module=instance)
        else:
            return

class SharedPrograms(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='share_programs')
    shared_programs = models.ForeignKey(Program,on_delete=models.CASCADE,related_name='shared_programmes', null=True,blank=True )
    shared_level = models.CharField(max_length=10,choices=levels,null=True,blank=True)

sex = (('Male','Male'),('Female','Female'),('Other','Other'))
#Student table
class Student(models.Model):
    reg_number = models.CharField(max_length=8, unique=True)
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices = sex)
    dob = models.DateField()
    address = models.TextField()
    programme_code = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='program_students')
    level = models.CharField(max_length=10,choices=levels)
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.surname} {self.firstname}'

    #register modules
    def registration(self):
        if not self.is_registered:
            #get program
            _program = Program.objects.get(id = self.reg_number)
            #get modules
            modules = _program.program_modules.filter(level= self.level)
            for module in modules:
                reg_module = Registration.objects.get(module= module)
                reg_module.no_of_students += 1
                reg_module.students.add(self.id)
                reg_module.save()

            self.is_registered = True

#Registration Table
class Registration(models.Model):
    module = models.ForeignKey(Module,on_delete=models.CASCADE,related_name='registered_students')
    no_of_students = models.IntegerField(default=0)
    students = models.ManyToManyField(Student,related_name='registered_students',null=True,blank =True)
    def __str__(self):
        return f'{self.module} {self.no_of_students}'

#Invigilators Table
class Invigilator(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department_invigilators')
    name = models.CharField(max_length=25)
    ec_number = models.CharField(max_length=25,unique=True)
    is_available = models.BooleanField(default=True)

    def get_dept_id(self):return self.department
    def get_name(self):return self.name
    def get_name(self):return self.ec_number
    def __str__(self): return self.name

#Room Table 
class Room(models.Model):
    room_number = models.CharField(max_length=25,unique=True)
    seating_capacity = models.IntegerField()
    venue = models.CharField(max_length=25,unique=True)
    is_available = models.BooleanField(default=True)
    def get_room_number(self):return self.room_number
    def get_seating_capacity(self):return self.seating_capacity
    def get_venue(self):return self.venue
    def __str__(self):return f'{self.room_number} ({self.seating_capacity})'

#Session Table
class Session(models.Model):
    session_id = models.CharField(max_length=25,null=True)
    date = models.DateField(null=True)
    time = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def set_date(self,date):self.date =date
    def get_session_id(self):return self.session_id
    def get_date(self):return self.date
    def get_time(self):return self.time
    # def __str__(self): return self.session_id

class Session1(models.Model):
    session_id = models.CharField(max_length=25,null=True)
    date = models.DateField(null=True)
    time = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def set_date(self,date):self.date =date
    def get_session_id(self):return self.session_id
    def get_date(self):return self.date
    def get_time(self):return self.time
    def __str__(self): return f"{self.date} {self.time}"




    
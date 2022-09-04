from django.db import models
from django.contrib.auth.models import User
import random
from Database.models import Department

# Create your models here.

levels = (
    ('Admins','Admins'),('Staff','Staff'),('hod','hod')
)
sex =(
    ('Male','Male'),('Female','Female')
)

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ec_number = models.CharField(max_length=8)
    gender = models.CharField(max_length=100,choices=sex)
    access_level = models.CharField(max_length=100, choices=levels)
    def __str__(self):return self.first_name

class Hod(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ec_number = models.CharField(max_length=8)
    gender = models.CharField(max_length=100,choices=sex)
    department = models.OneToOneField(Department, on_delete=models.CASCADE, related_name='department_hod')

class Codes(models.Model):
    code = models.CharField(max_length=5)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_code')

    def __str__(self): return self.code

    # generate a random code to validate the user when login
    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items =[]

        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)

        code_string = "".join(str(item) for item in code_items)
        self.code = code_string 
        super().save(*args, **kwargs)


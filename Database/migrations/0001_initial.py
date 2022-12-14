# Generated by Django 3.1 on 2022-06-18 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_code', models.CharField(max_length=10, unique=True)),
                ('department_name', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_code', models.CharField(max_length=10, unique=True)),
                ('faculty_name', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_code', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[('1.1', '1.1'), ('1.2', '1.2'), ('2.1', '2.1'), ('2.2', '2.2'), ('3.1', '3.1'), ('3.2', '3.2'), ('4.1', '4.1'), ('4.2', '4.2'), ('5.1', '5.1'), ('5.2', '5.2')], max_length=10)),
                ('module_credits', models.IntegerField()),
                ('isMassModule', models.BooleanField(default=False)),
                ('numOfStudents', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
                ('department_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_modules', to='Database.department')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programme_code', models.CharField(max_length=10, unique=True)),
                ('programme_name', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('department_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_programs', to='Database.department')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=25, unique=True)),
                ('seating_capacity', models.IntegerField()),
                ('venue', models.CharField(max_length=25, unique=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=25, unique=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(max_length=8, unique=True)),
                ('surname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('level', models.CharField(choices=[('1.1', '1.1'), ('1.2', '1.2'), ('2.1', '2.1'), ('2.2', '2.2'), ('3.1', '3.1'), ('3.2', '3.2'), ('4.1', '4.1'), ('4.2', '4.2'), ('5.1', '5.1'), ('5.2', '5.2')], max_length=10)),
                ('is_registered', models.BooleanField(default=False)),
                ('programme_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_students', to='Database.program')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_students', models.IntegerField(default=0)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registered_students', to='Database.module')),
                ('students', models.ManyToManyField(null=True, related_name='registered_students', to='Database.Student')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='programme_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_modules', to='Database.program'),
        ),
        migrations.AddField(
            model_name='module',
            name='shared_programs',
            field=models.ManyToManyField(null=True, related_name='shared_programmes', to='Database.Program'),
        ),
        migrations.CreateModel(
            name='Invigilator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('ec_number', models.CharField(max_length=25, unique=True)),
                ('is_available', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_invigilators', to='Database.department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='faculty_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_departments', to='Database.faculty'),
        ),
    ]

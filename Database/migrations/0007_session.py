# Generated by Django 3.1 on 2022-06-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0006_delete_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=25, unique=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
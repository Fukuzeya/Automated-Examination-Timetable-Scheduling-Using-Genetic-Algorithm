# Generated by Django 3.1 on 2022-06-28 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0009_auto_20220628_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_id',
            field=models.CharField(max_length=25, null=True),
        ),
    ]

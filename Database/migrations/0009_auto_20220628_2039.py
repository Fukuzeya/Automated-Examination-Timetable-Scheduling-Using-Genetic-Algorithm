# Generated by Django 3.1 on 2022-06-28 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0008_auto_20220628_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.1 on 2022-06-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0003_module_shared_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='borrowed',
            field=models.BooleanField(default=False),
        ),
    ]

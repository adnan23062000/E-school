# Generated by Django 2.2.5 on 2019-11-09 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gradesApp', '0002_auto_20191109_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_student',
        ),
    ]

# Generated by Django 4.2 on 2023-04-17 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EvaluateHub', '0015_alter_evaluationform_student_affairs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluationform',
            old_name='student_affairs',
            new_name='students_affairs',
        ),
    ]

# Generated by Django 5.0.3 on 2024-06-08 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examApp', '0002_rename_created_date_exam_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='number_of_questions',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='total_marks',
        ),
    ]

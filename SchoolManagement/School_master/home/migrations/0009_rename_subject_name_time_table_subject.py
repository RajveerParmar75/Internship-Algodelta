# Generated by Django 4.2.2 on 2023-06-10 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_standard_values_remove_teacher_subject_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time_table',
            old_name='subject_name',
            new_name='subject',
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_teacher_standard_alter_teacher_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.IntegerField(default=5)),
                ('subject_name', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=50)),
                ('slot', models.IntegerField()),
                ('teacher', models.IntegerField()),
            ],
        ),
    ]

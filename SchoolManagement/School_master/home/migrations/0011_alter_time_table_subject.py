# Generated by Django 4.2.2 on 2023-06-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_standard_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_table',
            name='subject',
            field=models.IntegerField(max_length=50),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-21 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentdata',
            name='header_id',
        ),
    ]

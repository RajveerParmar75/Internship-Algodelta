# Generated by Django 4.2.2 on 2023-06-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_customuser_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='standard',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='grade',
            field=models.FloatField(),
        ),
    ]

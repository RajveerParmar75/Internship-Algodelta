# Generated by Django 4.2.2 on 2023-06-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_user_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='log',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_blacklisttoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklisttoken',
            name='token',
            field=models.CharField(max_length=500),
        ),
    ]

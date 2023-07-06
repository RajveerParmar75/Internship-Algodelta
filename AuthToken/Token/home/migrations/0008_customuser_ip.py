# Generated by Django 4.2.1 on 2023-06-05 08:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_customuser_mac'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='ip',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
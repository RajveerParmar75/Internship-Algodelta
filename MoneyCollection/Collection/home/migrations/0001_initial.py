# Generated by Django 4.2.2 on 2023-07-01 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.IntegerField(default=0)),
                ('address', models.TextField()),
                ('proof', models.TextField()),
                ('loan_amount', models.IntegerField(default=0)),
                ('outstanding', models.IntegerField(default=0)),
                ('penalty', models.IntegerField(default=0)),
                ('days', models.IntegerField(default=0)),
                ('starting_date', models.DateTimeField()),
                ('ending_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_credited', models.BooleanField(default=True)),
                ('amount', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
    ]

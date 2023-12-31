# Generated by Django 4.2.3 on 2023-07-04 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saving_Transection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('done_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.agentuser')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.saving_account')),
            ],
        ),
    ]

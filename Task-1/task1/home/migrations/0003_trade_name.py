# Generated by Django 4.2.1 on 2023-05-29 04:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_trade_action_alter_trade_avg_alter_trade_p_l'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
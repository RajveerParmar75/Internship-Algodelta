# Generated by Django 4.2.1 on 2023-05-27 18:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time', models.TimeField(auto_now=True)),
                ('qnt', models.IntegerField()),
                ('price', models.FloatField()),
                ('action', models.CharField(max_length=3)),
                ('avg', models.FloatField()),
                ('p_l', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-05 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_loan_account_loan_transection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminuser',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='agentuser',
            old_name='admin_id',
            new_name='admin',
        ),
        migrations.RenameField(
            model_name='agentuser',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='loan_account',
            old_name='agent_id',
            new_name='agent',
        ),
        migrations.RenameField(
            model_name='loan_transection',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='saving_account',
            old_name='agent_id',
            new_name='agent',
        ),
        migrations.RenameField(
            model_name='saving_transection',
            old_name='user_id',
            new_name='user',
        ),
    ]

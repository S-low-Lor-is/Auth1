# Generated by Django 4.1.3 on 2023-01-04 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0006_account2_delete_account'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account2',
            new_name='Account',
        ),
    ]

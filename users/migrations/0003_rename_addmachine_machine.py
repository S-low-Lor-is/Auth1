# Generated by Django 4.1.3 on 2023-01-06 05:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_addmachine_delete_iddaw'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddMachine',
            new_name='Machine',
        ),
    ]

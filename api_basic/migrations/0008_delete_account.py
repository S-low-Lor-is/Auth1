# Generated by Django 4.1.3 on 2023-01-05 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0007_rename_account2_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]

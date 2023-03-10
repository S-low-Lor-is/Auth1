# Generated by Django 4.1.3 on 2023-01-06 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_sell'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.machine')),
            ],
        ),
    ]

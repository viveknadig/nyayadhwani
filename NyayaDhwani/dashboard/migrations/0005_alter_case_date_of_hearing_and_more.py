# Generated by Django 5.0.7 on 2024-08-02 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_case_date_of_hearing_alter_case_court_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='Date_of_hearing',
            field=models.DateField(default=datetime.datetime(2024, 8, 3, 19, 11, 13, 313208)),
        ),
        migrations.AlterField(
            model_name='register_case',
            name='Descriptions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
# Generated by Django 5.0.7 on 2024-07-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_case_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='Description',
            field=models.CharField(max_length=250),
        ),
    ]

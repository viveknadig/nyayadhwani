# Generated by Django 5.0.7 on 2024-07-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_register_case_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_case',
            name='proofs',
            field=models.ImageField(default='evid.png', upload_to='evidence_images'),
        ),
        migrations.AlterField(
            model_name='register_case',
            name='type_of_case',
            field=models.CharField(choices=[('Criminal', 'Criminal'), ('Family', 'Family'), ('Corporate', 'Corporate'), ('Civil', 'Civil'), ('Intellectual property', 'Intellectual property'), ('Cyber', 'Cyber'), ('Contract', 'Contract')], default='Criminal', max_length=100),
        ),
    ]
# Generated by Django 5.0.7 on 2024-07-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_register_case_proofs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_case',
            name='proofs',
            field=models.ImageField(default='evid.png', upload_to='evidence_images/'),
        ),
    ]

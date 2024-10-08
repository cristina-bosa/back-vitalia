# Generated by Django 5.0.6 on 2024-09-19 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0007_alter_appointmentinformation_medical_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentinformation',
            name='medical_appointment',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointment_information', to='doctors.medicalappointment'),
        ),
    ]

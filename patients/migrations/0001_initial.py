# Generated by Django 5.0.6 on 2024-08-11 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'allergy',
                'verbose_name_plural': 'allergies',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CurrentMedication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'current_medication',
                'verbose_name_plural': 'current_medications',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MedicalIntervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'medical_intervention',
                'verbose_name_plural': 'medical_interventiones',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RelevantDiseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'relevant_disease',
                'verbose_name_plural': 'relevant_diseases',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('allergies', models.ManyToManyField(blank=True, related_name='allergies', to='patients.allergies')),
                ('current_medication', models.ManyToManyField(blank=True, related_name='current_medication', to='patients.currentmedication')),
                ('medical_intervention', models.ManyToManyField(blank=True, related_name='medical_intervention', to='patients.medicalintervention')),
                ('relevant_diseases', models.ManyToManyField(blank=True, related_name='relevant_diseases', to='patients.relevantdiseases')),
            ],
            options={
                'verbose_name': 'medical_history',
                'verbose_name_plural': 'medical_histories',
            },
        ),
    ]

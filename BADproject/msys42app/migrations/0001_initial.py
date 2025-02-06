# Generated by Django 5.0.2 on 2025-02-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spc_code', models.CharField(max_length=300, unique=True)),
                ('spc_name', models.CharField(max_length=300)),
                ('spc_sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('spc_birth', models.DateField()),
                ('blood_group', models.CharField(blank=True, max_length=5, null=True)),
                ('address', models.TextField()),
                ('philhealth_number', models.CharField(blank=True, max_length=50, null=True)),
                ('fourps_number', models.CharField(blank=True, max_length=50, null=True)),
                ('guardian_name', models.CharField(max_length=300)),
                ('guardian_relationship', models.CharField(max_length=100)),
                ('guardian_sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]

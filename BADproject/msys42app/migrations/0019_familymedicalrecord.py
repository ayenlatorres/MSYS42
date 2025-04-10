# Generated by Django 5.0.2 on 2025-04-07 11:32

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msys42app', '0018_alter_familymember_child_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyMedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('age', models.PositiveSmallIntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=4)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=4)),
                ('bp', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(regex='^\\d{2,3}/\\d{2,3}$')])),
                ('temp', models.DecimalField(decimal_places=1, max_digits=3)),
                ('med_stat', models.CharField(max_length=50)),
                ('medication', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msys42app.familymember')),
            ],
        ),
    ]

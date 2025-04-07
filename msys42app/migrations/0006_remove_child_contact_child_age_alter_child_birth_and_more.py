# Generated by Django 5.0.2 on 2025-02-15 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msys42app', '0005_alter_child_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='contact',
        ),
        migrations.AddField(
            model_name='child',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='birth',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='ContactNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_numbers', to='msys42app.child')),
            ],
        ),
    ]

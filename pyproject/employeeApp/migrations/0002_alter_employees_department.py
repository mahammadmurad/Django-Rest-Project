# Generated by Django 5.0.2 on 2024-02-07 08:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeApp.departments'),
        ),
    ]
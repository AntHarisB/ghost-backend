# Generated by Django 4.2 on 2023-05-16 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PerformanceTab', '0005_projectinformation_costs_actual_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectinformation',
            name='margin',
        ),
    ]

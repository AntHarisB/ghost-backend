# Generated by Django 4.2 on 2023-05-25 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PerformanceTab', '0007_projectinformation_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectinformation',
            old_name='team_size',
            new_name='team_s',
        ),
    ]

# Generated by Django 4.2 on 2023-04-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PerformanceTab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_value', models.FloatField()),
                ('team_size', models.IntegerField()),
                ('velocity', models.IntegerField()),
                ('weeks_over_ddl', models.IntegerField()),
                ('hourly_price', models.IntegerField()),
                ('year', models.IntegerField()),
                ('lead_closing', models.FloatField()),
                ('project_creation', models.CharField(max_length=100)),
                ('type_of_project', models.CharField(max_length=100)),
                ('hours_available', models.IntegerField()),
                ('hours_billed', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectDetails',
        ),
    ]
# Generated by Django 4.2 on 2023-05-13 15:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PerformanceTab', '0003_projectinformation_date_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinformation',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
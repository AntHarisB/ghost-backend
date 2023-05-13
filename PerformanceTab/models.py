from django.db import models

class ProjectInformation (models.Model):

    project_name = models.CharField(max_length=100)
    project_value = models.FloatField()
    team_size = models.IntegerField()
    velocity = models.IntegerField()
    weeks_over_ddl = models.IntegerField()
    hourly_price = models.IntegerField()
    year = models.IntegerField()
    lead_closing = models.FloatField()
    project_creation = models.CharField(max_length=100)
    type_of_project = models.CharField(max_length=100)
    hours_available = models.IntegerField()
    hours_billed = models.IntegerField()
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    members = models.ManyToManyField('auth.User')

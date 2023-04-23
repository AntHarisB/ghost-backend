from django.db import models

class Performance (models.Model):

    project_name = models.CharField(max_length=100)
    project_value = models.FloatField()
    team_size = models.IntegerField()
    velocity = models.IntegerField()
    weeks_over_ddl = models.IntegerField()
    hourly_price = models.IntegerField()
    year = models.IntegerField()

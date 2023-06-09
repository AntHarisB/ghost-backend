from decimal import Decimal
from django.db import models

class ProjectInformation (models.Model):

    project_name = models.CharField(max_length=100)
    project_value = models.FloatField()
    team_s = models.IntegerField(blank=True, null=True)
    velocity = models.IntegerField()
    weeks_over_ddl = models.IntegerField()
    hourly_price = models.IntegerField(null=True)
    year = models.IntegerField()
    lead_closing = models.FloatField()
    project_creation = models.CharField(max_length=100)
    type_of_project = models.CharField(max_length=100)
    hours_available = models.IntegerField()
    hours_billed = models.IntegerField()
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    members = models.ManyToManyField('auth.User')
    project_value_planned = models.FloatField(null=True)
    costs_planned = models.FloatField(null=True)
    costs_actual = models.FloatField(null=True)
    development = models.FloatField(null=True)
    design = models.FloatField(null=True)
    other = models.FloatField(null=True)
    total_revenue = models.FloatField(null=True)
    direct = models.FloatField(null=True)
    indirect = models.FloatField(null=True)
    marketing = models.FloatField(null=True)
    HRcost = models.FloatField(null=True)
    officeCost = models.FloatField(null=True)
    salesCosts = models.FloatField(null=True)
    otherCosts = models.FloatField(null=True)
    margin = models.FloatField(null=True)
    description = models.CharField(max_length=255, null=True)
    status = models.CharField (max_length=100, null=True)


    @property
    def margin(self):
        if self.project_value and self.costs_actual:
            return (self.costs_actual / self.project_value) * 100
        return None
    

    

    




from django.db import models

class Invoicing(models.Model):
    client = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    total_hours_billed = models.IntegerField()
    amount_billed = models.FloatField()
    status = models.CharField(max_length=50)
    paid = models.CharField(max_length=10)
    sent = models.CharField(max_length=10)
    

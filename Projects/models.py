from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.URLField(blank=True)
    department = models.CharField(max_length=100, blank=True)
    monthly_salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    tech_stack = models.CharField(max_length=100, blank=True)



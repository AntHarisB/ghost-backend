from django.db import models
from PerformanceTab.models import ProjectInformation
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectInformation, on_delete=models.CASCADE)
    employment_type = models.CharField(max_length=50)
from rest_framework import serializers
from PerformanceTab.models import ProjectInformation

class ActualRevenueCostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInformation
        fields = ['project_name', 'project_value', 'costs_actual']
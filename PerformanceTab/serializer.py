from rest_framework import serializers
from .models import ProjectInformation

class ProjectSerializer(serializers.ModelSerializer):
    total_projects = serializers.SerializerMethodField()
    total_value = serializers.SerializerMethodField()
    avg_value = serializers.SerializerMethodField()
    avg_lead_closing = serializers.SerializerMethodField()
    avg_team_size = serializers.SerializerMethodField()
    avg_velocity = serializers.SerializerMethodField()
    weeks_over_ddl = serializers.SerializerMethodField()
    avg_hourly_price = serializers.SerializerMethodField()

    def get_total_projects(self, obj):
        return obj['total_projects']

    def get_total_value(self, obj):
        return obj['total_value']

    def get_avg_value(self, obj):
        return obj['avg_value']

    def get_avg_lead_closing(self, obj):
        return obj['avg_lead_closing']

    def get_avg_team_size(self, obj):
        return obj['avg_team_size']

    def get_avg_velocity(self, obj):
        return obj['avg_velocity']

    def get_weeks_over_ddl(self, obj):
        return obj['weeks_over_ddl']

    def get_avg_hourly_price(self, obj):
        return obj['avg_hourly_price']
    
    class Meta:
        model = ProjectInformation
        fields = ['total_projects', 'total_value', 'avg_value', 'avg_lead_closing', 'avg_team_size', 'avg_velocity', 'weeks_over_ddl', 'avg_hourly_price']

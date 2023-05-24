from rest_framework import serializers
from PerformanceTab.models import ProjectInformation

class ProjectInfoSerializer(serializers.ModelSerializer):
    total_projects = serializers.SerializerMethodField()
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    
    def get_total_projects(self, obj):
        return ProjectInformation.objects.count()

    def get_start(self, obj):
        date_start = obj.date_start
        start = date_start.strftime("%b %Y")
        return start
    
    def get_end(self, obj):
        date_end = obj.date_end
        end = date_end.strftime("%b %Y")
        return end
    
    class Meta:
        model = ProjectInformation
        fields = ['total_projects', 'project_name', 'description', 'start', 'end', 'team_size', 'project_value', 'status', 'hourly_price']

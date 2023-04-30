from rest_framework import serializers
from .models import ProjectInformation

class ProjectTypeSerializer(serializers.Serializer):
    total_projects = serializers.SerializerMethodField()
    num_of_fixed_projects = serializers.SerializerMethodField()
    num_of_ongoing_projects = serializers.SerializerMethodField()

    def get_num_of_fixed_projects(self, obj):
        year = self.context['year']
        return ProjectInformation.objects.filter(year=year, type_of_project='fixed').count()

    def get_num_of_ongoing_projects(self, obj):
        year = self.context['year']
        return ProjectInformation.objects.filter(year=year, type_of_project='on-going').count()
    
    def get_total_projects(self, obj):
        year = self.context['year']
        return ProjectInformation.objects.filter(year=year).count()
    
    class Meta:
        model = ProjectInformation
        fields = ['num_of_fixed_projects', 'num_of_ongoing_projects', 'total_projects']
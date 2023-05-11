from rest_framework import serializers
from .models import ProjectInformation

class ProjectCreationSerializer(serializers.Serializer):
    total_projects = serializers.SerializerMethodField()
    num_of_recommendation_projects = serializers.SerializerMethodField()
    num_of_partnership_projects = serializers.SerializerMethodField()
    num_of_sales_projects = serializers.SerializerMethodField()

    def get_num_of_recommendation_projects(self, obj):
        year = self.context['year']
        return ProjectInformation.objects.filter(year=year, project_creation='preporuka').count()

    def get_num_of_partnership_projects(self, obj):
        year = self.context['year']
        return ProjectInformation.objects.filter(year=year, project_creation='partnerstvo').count()

    def get_num_of_sales_projects(self, obj):
        year = self.context['year']
        return ProjectInformation.objects.filter(year=year, project_creation='prodaja').count()
    
    def get_total_projects(self, obj):
        year = self.context['year']
        return ProjectInformation.objects.filter(year=year).count()
    
    class Meta:
        model = ProjectInformation
        fields = ['num_of_recommendation_projects', 'num_of_partnership_projects', 'num_of_sales_projects', 'total_projects']
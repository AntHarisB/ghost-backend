from rest_framework import serializers
from django.contrib.auth.models import User
from PerformanceTab.models import ProjectInformation
from RevenueCosts.models import Member

class EmployeeIdSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='profile.department')
    monthly_salary = serializers.IntegerField(source='profile.monthly_salary')
    tech_stack = serializers.CharField(source='profile.tech_stack')
    profile_photo = serializers.URLField(source='profile.profile_photo')
    projects = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'department', 'monthly_salary', 'tech_stack', 'profile_photo', 'projects')

    def get_projects(self, obj):
        projects = []
        memberships = Member.objects.filter(user=obj)
        for membership in memberships:
            project_id = membership.project_id
            project = ProjectInformation.objects.get(id=project_id)
            project_data = {
                'project_name': project.project_name,
                'employment_type': membership.employment_type
            }
            projects.append(project_data)
        return projects

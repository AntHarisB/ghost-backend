from rest_framework import serializers
from PerformanceTab.models import ProjectInformation
from .models import Profile

class ProjectInfoSerializer(serializers.ModelSerializer):
    total_projects = serializers.SerializerMethodField()
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()
    team_size = serializers.SerializerMethodField()

    def get_users(self, obj):
        members = obj.members.all()
        users_data = []
        for member in members:
            profile = Profile.objects.get(user=member.user)
            user_data = {
                'first_name': member.user.first_name,
                'last_name': member.user.last_name,
                'profile_image': profile.profile_photo if profile else None
            }
            users_data.append(user_data)
        return users_data
    
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
    
    def get_team_size(self, obj):
        return obj.team_s
    
    class Meta:
        model = ProjectInformation
        fields = ['total_projects', 'project_name', 'description', 'start', 'end', 'team_size', 'project_value', 'status', 'hourly_price']

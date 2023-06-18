from rest_framework import serializers
from PerformanceTab.models import ProjectInformation
from .models import Profile
from django.contrib.auth.models import User

class OnholdProjectInfoSerializer(serializers.ModelSerializer):
    total_projects = serializers.SerializerMethodField()
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()

    def get_users(self, obj):
        members = obj.members.all()
        users_data = []
        for member in members:
            profile = Profile.objects.get(user=member)
            users_data.append({
                'first_name': member.first_name,
                'last_name': member.last_name,
                'profile_photo': profile.profile_photo,
            })

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
    
    
    class Meta:
        model = ProjectInformation
        fields = ['total_projects', 'project_name', 'description', 'start', 'end', 'team_s', 'project_value', 'status', 'hourly_price', 'users']

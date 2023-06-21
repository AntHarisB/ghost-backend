from rest_framework import serializers
from PerformanceTab.models import ProjectInformation
from RevenueCosts.models import Member

class MemberSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    employment_type = serializers.CharField(max_length=50)

class ProjectCreateSerializer(serializers.Serializer):
    project_name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    status = serializers.CharField(max_length=100)
    hourly_price = serializers.IntegerField()
    project_value = serializers.FloatField()
    members = MemberSerializer(many=True)

    def create(self, validated_data):
        members_data = validated_data.pop('members')
        project = ProjectInformation.objects.create(**validated_data)
        
        for member_data in members_data:
            user_id = member_data['user_id']
            employment_type = member_data['employment_type']
            member = Member.objects.create(user_id=user_id, project=project, employment_type=employment_type)

        return project

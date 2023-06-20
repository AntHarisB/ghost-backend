from PerformanceTab.models import ProjectInformation
from rest_framework import serializers
from RevenueCosts.models import Member
from django.contrib.auth.models import User

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['user', 'employment_type']

class ProjectUpdateSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, required=False)

    class Meta:
        model = ProjectInformation
        fields = ['project_name', 'description', 'date_start', 'date_end', 'status', 'hourly_price', 'project_value', 'members']

    def update(self, instance, validated_data):
        members_data = validated_data.pop('members', [])
        existing_members = list(instance.member_set.all())
        
        for member_data in members_data:
            user = member_data['user']
            employment_type = member_data['employment_type']

            for member in existing_members:
                if member.user == user:
                    member.employment_type = employment_type
                    member.save()
                    break
            else:
                Member.objects.create(user=user, project=instance, employment_type=employment_type)

        Member.objects.filter(project=instance).exclude(user__in=[member_data['user'] for member_data in members_data]).delete()

        return super().update(instance, validated_data)
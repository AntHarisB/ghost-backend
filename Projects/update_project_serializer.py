from PerformanceTab.models import ProjectInformation
from rest_framework import serializers

class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInformation
        fields = ['project_name', 'description', 'date_start', 'date_end', 'status', 'hourly_price', 'project_value', 'members']

    def save(self, **kwargs):
        members = self.validated_data.get('members')
        instance = super().save(**kwargs)

        if members is not None:
            instance.members.set(members)

        return instance


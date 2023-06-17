from rest_framework import serializers
from django.contrib.auth.models import User
from PerformanceTab.models import ProjectInformation

class ProjectInformationSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = ProjectInformation
        fields = '__all__'

class ProjectCreateSerializer(serializers.Serializer):
    project_name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    status = serializers.CharField(max_length=100)
    hourly_price = serializers.IntegerField()
    project_value = serializers.FloatField()
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    def create(self, validated_data):
        members_data = validated_data.pop('members')
        project = ProjectInformation.objects.create(**validated_data)

        for member in members_data:
            project.members.add(member)

        return project




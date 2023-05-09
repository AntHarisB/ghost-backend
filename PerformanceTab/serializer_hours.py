from rest_framework import serializers
from .models import ProjectInformation
from datetime import datetime

class ProjectHoursSerializer(serializers.Serializer):

    date_start = serializers.SerializerMethodField()
    month = serializers.SerializerMethodField()
    hours_available = serializers.IntegerField()
    hours_billed = serializers.IntegerField()
    project_name = serializers.CharField()
    type_of_project = serializers.CharField()
    id = serializers.IntegerField()

    def get_date_start(self, obj):
        date_start_str = obj.date_start.strftime('%d-%m-%Y')
        return date_start_str

    def get_month(self, obj):
        date_start = obj.date_start
        month_name = date_start.strftime("%B")
        return month_name
    
    class Meta:
        model = ProjectInformation
        fields = ['id', 'project_name', 'hours_available', 'hours_billed', 'date_start ', 'month', 'type_of_project']
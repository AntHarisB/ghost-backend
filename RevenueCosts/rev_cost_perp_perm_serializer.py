from rest_framework import serializers
from PerformanceTab.models import ProjectInformation
from datetime import date, timedelta
from django.db.models import Q

class ActualRevenueCostsMonthSerializer(serializers.ModelSerializer):
    revenue_gap = serializers.SerializerMethodField()
    month = serializers.SerializerMethodField()
    date_project = serializers.SerializerMethodField()
    month_name = serializers.SerializerMethodField()
    actual_avg_margin = serializers.SerializerMethodField()

    def get_date_project(self, obj):
        date_project_str = obj.date_start.strftime('%d-%m-%Y')
        return date_project_str
    
    def get_month_name(self, obj):
        date_start = obj.date_start
        month_name = date_start.strftime("%B")
        return month_name

    def get_revenue_gap(self, obj):
        project_value = obj.project_value
        project_value_planned = obj.project_value_planned
        if project_value is not None and project_value_planned is not None:
            return round(project_value - project_value_planned,2)
        return None
    
    def get_month(self, obj):
        today = date.today()
        current_month = today.month
        previous_month = current_month - 1 if current_month > 1 else 12
        next_month = current_month + 1 if current_month < 12 else 1

        start_month = obj.date_start.month if obj.date_start else None

        if start_month in [previous_month, current_month, next_month]:
            return start_month
        return None
    
    class Meta:
        model = ProjectInformation
        fields = ['costs_actual', 'costs_planned', 'project_value', 'project_value_planned', 'revenue_gap', 'month', 'month_name', 'date_project', 'actual_avg_margin']
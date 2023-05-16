from rest_framework import serializers
from PerformanceTab.models import ProjectInformation
from django.db.models import Avg, Sum

class StatsRevenueCostSerializer(serializers.Serializer):
    actual_revenue = serializers.SerializerMethodField()
    planned_direct_cost = serializers.SerializerMethodField()
    margin = serializers.SerializerMethodField()
    actual_gross_profit = serializers.SerializerMethodField()
    
    def get_actual_revenue(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(actual_revenue=Sum('project_value'))
        return project['actual_revenue']
    
    def get_planned_direct_cost(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(planned_direct_cost=Sum('costs_planned'))
        return project['planned_direct_cost']
    
    def get_margin(self, obj):
        actual_revenue = self.get_actual_revenue(obj)
        planned_direct_cost = self.get_planned_direct_cost(obj)
        if actual_revenue and planned_direct_cost:
            return (actual_revenue / planned_direct_cost) * 100
        return None
    
    def get_actual_gross_profit(self, obj):
        actual_revenue = self.get_actual_revenue(obj)
        planned_direct_cost = self.get_planned_direct_cost(obj)
        if actual_revenue and planned_direct_cost:
            return actual_revenue - planned_direct_cost
        return None
    
    class Meta:
        model = ProjectInformation
        fields = ['actual_revenue', 'planned_direct_cost', 'margin', 'actual_gross_profit']


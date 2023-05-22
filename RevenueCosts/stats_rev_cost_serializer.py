from rest_framework import serializers
from PerformanceTab.models import ProjectInformation
from django.db.models import Sum

class StatsRevenueCostSerializer(serializers.Serializer):
    actual_revenue = serializers.SerializerMethodField()
    planned_revenue = serializers.SerializerMethodField()
    planned_direct_cost = serializers.SerializerMethodField()
    actual_direct_cost = serializers.SerializerMethodField()
    margin = serializers.SerializerMethodField()
    actual_gross_profit = serializers.SerializerMethodField()
    actual_avg_margin = serializers.SerializerMethodField()
    
    def get_actual_revenue(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(actual_revenue=Sum('project_value'))
        return round(project['actual_revenue'], 2)
    
    def get_planned_revenue(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(planned_revenue=Sum('project_value_planned'))
        return round(project['planned_revenue'], 2)
    
    def get_actual_direct_cost(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(actual_direct_cost=Sum('costs_actual'))
        return round(project['actual_direct_cost'], 2)
    
    def get_planned_direct_cost(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(planned_direct_cost=Sum('costs_planned'))
        return round(project['planned_direct_cost'], 2)
    
    def get_margin(self, obj):
        actual_revenue = self.get_actual_revenue(obj)
        actual_direct_cost = self.get_actual_direct_cost(obj)
        margin_1 = actual_direct_cost / actual_revenue
        margin = margin_1*100
        rounded_margin = round(margin)
        return int(rounded_margin)
    
    def get_actual_gross_profit(self, obj):
        actual_revenue = self.get_actual_revenue(obj)
        planned_direct_cost = self.get_planned_direct_cost(obj)
        if actual_revenue and planned_direct_cost:
            rounded_gross = round(actual_revenue - planned_direct_cost, 2)
            return rounded_gross
        return None
    
    def get_actual_avg_margin(self, obj):
        year = self.context['year']
        projects = self.Meta.model.objects.filter(date_start__year=year)
        projects_count = projects.count()

        if projects_count > 0:
            margins = [item.costs_actual / item.project_value for item in projects]
            total_margin = sum(margins)
            avg_margin = total_margin / projects_count
            return round(avg_margin, 2)

        return None
    
    class Meta:
        model = ProjectInformation
        fields = ['actual_revenue', 'planned_direct_cost', 'margin', 'actual_gross_profit', 'actual_avg_margin']


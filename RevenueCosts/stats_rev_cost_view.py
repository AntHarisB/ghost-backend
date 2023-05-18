from rest_framework import generics
from PerformanceTab.models import ProjectInformation
from django.db.models import Avg, Sum
from rest_framework.response import Response
from .stats_rev_cost_serializer import StatsRevenueCostSerializer

class StatsRevenueCost(generics.ListAPIView):
    serializer_class = StatsRevenueCostSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = ProjectInformation.objects.filter(year=year)[:1]
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['year'] = self.kwargs['year']
        return context



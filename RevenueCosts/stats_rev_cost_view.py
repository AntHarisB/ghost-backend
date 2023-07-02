from rest_framework import generics
from PerformanceTab.models import ProjectInformation
from rest_framework.permissions import IsAuthenticated
from .stats_rev_cost_serializer import StatsRevenueCostSerializer
from django.db.models.functions import ExtractYear

class StatsRevenueCost(generics.ListAPIView):
    serializer_class = StatsRevenueCostSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        year = self.kwargs['year']
        ProjectInformation.objects.update(year=ExtractYear('date_start'))
        queryset = ProjectInformation.objects.filter(year=year)[:1]
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['year'] = self.kwargs['year']
        return context



from rest_framework import generics
from PerformanceTab.models import ProjectInformation
from .rev_cost_perp_serializer import ActualRevenueCostsSerializer

class ActualRevenueCosts(generics.ListAPIView):
    serializer_class = ActualRevenueCostsSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = ProjectInformation.objects.filter(year=year)
        return queryset

    def get_serializer_context(self):
        return {'year': self.kwargs['year']}

from rest_framework import generics
from PerformanceTab.models import ProjectInformation
from .rev_cost_perp_serializer import ActualRevenueCostsSerializer
from rest_framework.permissions import IsAuthenticated

class ActualRevenueCosts(generics.ListAPIView):
    serializer_class = ActualRevenueCostsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = ProjectInformation.objects.filter(year=year)
        return queryset

    def get_serializer_context(self):
        return {'year': self.kwargs['year']}

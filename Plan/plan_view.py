from rest_framework import generics
from PerformanceTab.models import ProjectInformation
from .plan_serializer import PlanSerializer
from rest_framework.permissions import IsAuthenticated

class Plan(generics.ListAPIView):
    serializer_class = PlanSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = ProjectInformation.objects.filter(year=year)[:1]
        return queryset

    def get_serializer_context(self):
        return {'year': self.kwargs['year']}

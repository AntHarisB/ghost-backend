from rest_framework import generics
from PerformanceTab.models import ProjectInformation
from .plan_serializer import PlanSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

class Plan(generics.ListAPIView):
    serializer_class = PlanSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        current_year = timezone.now().year
        queryset = ProjectInformation.objects.filter(year=current_year)[:1]
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['year'] = timezone.now().year
        return context

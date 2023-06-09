from rest_framework import generics
from PerformanceTab.models import ProjectInformation
from datetime import date
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .rev_cost_perp_perm_serializer import ActualRevenueCostsMonthSerializer
from django.db.models.functions import ExtractYear

class RevenueCostPerMonth(generics.ListAPIView):
    serializer_class = ActualRevenueCostsMonthSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        year = self.kwargs['year']
        ProjectInformation.objects.update(year=ExtractYear('date_start'))
        today = date.today()
        current_month = today.month

        previous_month = current_month - 1 if current_month > 1 else 12
        next_month = current_month + 1 if current_month < 12 else 1

        queryset = ProjectInformation.objects.filter(
         Q(date_start__year=year, date_start__month__in=[previous_month, current_month, next_month])
        )
        return queryset

    def get_serializer_context(self):
        return {'year': self.kwargs['year']}
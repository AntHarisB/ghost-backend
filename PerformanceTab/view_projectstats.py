from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import ProjectInformation
from .serializer_stats import ProjectSerializer
from django.db.models import Avg, Sum, Count

class ProjectStats(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = ProjectInformation.objects.filter(year=year)
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total_projects = len(queryset)
        stats = {
            'total_projects': total_projects,
            'total_value': queryset.aggregate(Sum('project_value'))['project_value__sum'],
            'avg_value': queryset.aggregate(Avg('project_value'))['project_value__avg'],
            'avg_lead_closing': queryset.aggregate(Avg('lead_closing'))['lead_closing__avg'],
            'avg_team_size': queryset.aggregate(Avg('team_size'))['team_size__avg'],
            'avg_velocity': queryset.aggregate(Avg('velocity'))['velocity__avg'],
            'weeks_over_ddl': queryset.aggregate(Avg('weeks_over_ddl'))['weeks_over_ddl__avg'],
            'avg_hourly_price': queryset.aggregate(Avg('hourly_price'))['hourly_price__avg']
        }
        serializer = self.get_serializer(stats)
        return Response(serializer.data)

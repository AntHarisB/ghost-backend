from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ProjectInformation
from .serializer_stats import ProjectSerializer
from django.db.models import Avg, Sum
from django.db.models import Count

class ProjectStats(generics.ListAPIView):
    serializer_class = ProjectSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = ProjectInformation.objects.filter(year=year)
        
        for project in queryset:
            team_size = project.members.count()
            project.team_s = team_size
            project.save()
        
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total_projects = len(queryset)
        avg_team_size = queryset.aggregate(avg_team_size=Avg('team_s'))['avg_team_size']
        stats = {
            'total_projects': total_projects,
            'total_value': queryset.aggregate(Sum('project_value'))['project_value__sum'],
            'avg_value': queryset.aggregate(Avg('project_value'))['project_value__avg'],
            'avg_lead_closing': queryset.aggregate(Avg('lead_closing'))['lead_closing__avg'],
            'avg_team_size': avg_team_size,
            'avg_velocity': queryset.aggregate(Avg('velocity'))['velocity__avg'],
            'weeks_over_ddl': queryset.aggregate(Avg('weeks_over_ddl'))['weeks_over_ddl__avg'],
            'avg_hourly_price': queryset.aggregate(Avg('hourly_price'))['hourly_price__avg']
        }
        serializer = self.get_serializer(stats)
        return Response(serializer.data)

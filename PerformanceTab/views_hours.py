from rest_framework import generics
from .models import ProjectInformation
from .serializer_hours import ProjectHoursSerializer

class ProjectHours(generics.ListAPIView):
    serializer_class = ProjectHoursSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = ProjectInformation.objects.filter(year=year)
        return queryset

    def get_serializer_context(self):
        return {'year': self.kwargs['year']}
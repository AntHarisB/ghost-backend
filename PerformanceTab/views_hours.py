from rest_framework import generics
from .models import ProjectInformation
from .serializer_hours import ProjectHoursSerializer
from rest_framework.permissions import IsAuthenticated

class ProjectHours(generics.ListAPIView):
    serializer_class = ProjectHoursSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = ProjectInformation.objects.filter(year=year, type_of_project='fixed')
        return queryset

    def get_serializer_context(self):
        return {'year': self.kwargs['year']}
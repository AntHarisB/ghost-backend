from rest_framework import generics
from .models import ProjectInformation
from .serializer_typeofproject import ProjectTypeSerializer

class ProjectTypeCount(generics.ListAPIView):
    serializer_class = ProjectTypeSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = ProjectInformation.objects.filter(year=year)[:1]
        return queryset

    def get_serializer_context(self):
        return {'year': self.kwargs['year']}
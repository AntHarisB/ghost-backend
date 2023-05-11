from rest_framework import generics
from .models import ProjectInformation
from .serializer_projcreation import ProjectCreationSerializer
from rest_framework.permissions import IsAuthenticated

class ProjectCreationCount(generics.ListAPIView):
    serializer_class = ProjectCreationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = ProjectInformation.objects.filter(year=year)[:1]
        return queryset

    def get_serializer_context(self):
        return {'year': self.kwargs['year']}
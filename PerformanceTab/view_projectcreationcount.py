from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import ProjectInformation
from .serializer_projcreation import ProjectCreationSerializer
from django.db.models import Avg, Sum, Count

class ProjectCreationCount(generics.ListAPIView):
    serializer_class = ProjectCreationSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = ProjectInformation.objects.filter(year=year)[:1]
        return queryset

    def get_serializer_context(self):
        return {'year': self.kwargs['year']}
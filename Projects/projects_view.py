from rest_framework import generics
from PerformanceTab.models import ProjectInformation
from .projects_serializer import ProjectInfoSerializer
from rest_framework.permissions import IsAuthenticated

class ProjectInfo(generics.ListAPIView):
    serializer_class = ProjectInfoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ProjectInformation.objects.all()

    

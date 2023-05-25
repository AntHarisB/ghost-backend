from rest_framework import generics
from PerformanceTab.models import ProjectInformation
from .projects_serializer import ProjectInfoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Profile

class ProjectInfo(generics.ListAPIView):
    serializer_class = ProjectInfoSerializer
    # permission_classes = (IsAuthenticated,)
    queryset = ProjectInformation.objects.all()

    

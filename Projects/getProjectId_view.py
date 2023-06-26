from rest_framework import generics
from PerformanceTab.models import ProjectInformation
from .projects_serializer import ProjectInfoSerializer
from django.shortcuts import get_object_or_404

class ProjectId(generics.RetrieveAPIView):
    serializer_class = ProjectInfoSerializer
    #permission_classes = (IsAuthenticated,)
    queryset = ProjectInformation.objects.all()

    def get_object(self):
        project_id = self.kwargs.get('id')
        return get_object_or_404(self.queryset, id=project_id)
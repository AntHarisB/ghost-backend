from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from PerformanceTab.models import ProjectInformation
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from .update_project_serializer import ProjectUpdateSerializer
from django.shortcuts import get_object_or_404

@permission_classes((permissions.AllowAny,))
class ProjectUpdateView(APIView):
    def put(self, request, project_id, format=None):
        project = get_object_or_404(ProjectInformation, id=project_id)
        serializer = ProjectUpdateSerializer(project, data=request.data, partial=True)  
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'success': 'Project updated!'}, status=status.HTTP_200_OK)

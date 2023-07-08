from PerformanceTab.models import ProjectInformation
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes


@permission_classes((permissions.AllowAny,))
class ProjectDeleteView(APIView):
    queryset = ProjectInformation.objects.all()

    def delete(self, request, project_id, format=None):
        try:
            project = ProjectInformation.objects.get(id=project_id)
        except ProjectInformation.DoesNotExist:
            raise Http404

        project.members.clear()
        project.delete()

        return Response({'success': 'Project deleted!'}, status=status.HTTP_204_NO_CONTENT)

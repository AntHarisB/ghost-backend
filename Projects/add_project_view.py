from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .add_project_serializer import ProjectCreateSerializer
from PerformanceTab.models import ProjectInformation
from rest_framework import permissions
from rest_framework.decorators import permission_classes


@permission_classes((permissions.AllowAny,))
class ProjectCreateView(APIView):
    def post(self, request, format=None):
        serializer = ProjectCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        project = ProjectInformation.objects.create(
            project_name=serializer.validated_data['project_name'],
            description=serializer.validated_data['description'],
            date_start=serializer.validated_data['date_start'],
            date_end=serializer.validated_data['date_end'],
            status=serializer.validated_data['status'],
            hourly_price=serializer.validated_data['hourly_price'],
            project_value=serializer.validated_data['project_value'],
            velocity=0,
            weeks_over_ddl=0,
            year=0,
            lead_closing=0,
            hours_available=0,
            hours_billed=0
        )

        for user in serializer.validated_data['members']:
            project.members.add(user)

        return Response({'success': 'Project created!'}, status=status.HTTP_201_CREATED)

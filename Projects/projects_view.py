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

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = serializer.data

        for i, project_data in enumerate(response_data):
            project = queryset[i]
            members = project.members.all()
            users_data = []
            for member in members:
                profile = Profile.objects.get(user=member.user)
                user_data = {
                    'first_name': member.user.first_name,
                    'last_name': member.user.last_name,
                    'profile_image': profile.profile_photo if profile else None
                }
                users_data.append(user_data)
            project_data['users'] = users_data

        return Response(response_data)

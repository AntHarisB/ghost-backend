from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .edit_employee_serializer import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import permission_classes

@permission_classes((permissions.AllowAny,))

class EmployeeUpdateView(APIView):
    def get_object(self, user_id):
        return get_object_or_404(User, id=user_id)

    def put(self, request, user_id, format=None):
        instance = self.get_object(user_id)
        user_serializer = UserSerializer(instance, data=request.data, partial=True)
        profile_instance = instance.profile
        profile_data = {
            'monthly_salary': request.data.get('monthly_salary', profile_instance.monthly_salary),
            'department': request.data.get('department', profile_instance.department),
            'tech_stack': request.data.get('tech_stack', profile_instance.tech_stack)
        }
        profile_serializer = ProfileSerializer(profile_instance, data=profile_data, partial=True)

        if user_serializer.is_valid() and profile_serializer.is_valid():
            user_serializer.save()
            profile_serializer.save()
            return Response(user_serializer.data)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

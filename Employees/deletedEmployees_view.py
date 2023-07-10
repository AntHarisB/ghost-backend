from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from .employee_serializer import EmployeeSerializer

class PastEmployeesList(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        past_employees = User.objects.filter(profile__obrisan=True)
        serializer = EmployeeSerializer(past_employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .edit_employee_serializer import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import permission_classes

@permission_classes((permissions.AllowAny,))

class EmployeeUpdateView(APIView):
    def get_object(self, user_id):
        return get_object_or_404(User, id=user_id)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = UserSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











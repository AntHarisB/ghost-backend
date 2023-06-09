from rest_framework.response import Response
from .add_employee_serializer import AddUserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import permission_classes


@permission_classes((permissions.AllowAny,))
class EmployeeAddView(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'), 
            'last_name': request.data.get('last_name'), 
            'profile': {
                'profile_photo': request.data.get('profile_photo'),
                'department': request.data.get('department'), 
                'monthly_salary': request.data.get('monthly_salary'), 
                'tech_stack': request.data.get('tech_stack')
            }
        }
        serializer = AddUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

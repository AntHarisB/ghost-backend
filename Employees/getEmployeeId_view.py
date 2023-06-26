from rest_framework import generics
from .getEmployeeId_serializer import EmployeeIdSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class EmployeeId(generics.RetrieveAPIView):  
    serializer_class = EmployeeIdSerializer
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def get_object(self):
        user_id = self.kwargs.get('id')
        return get_object_or_404(self.queryset, id=user_id)
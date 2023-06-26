from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .employee_serializer import EmployeeSerializer
from django.contrib.auth.models import User

class ProjectInfoPagination(PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })

class Employee(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    #permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    pagination_class = ProjectInfoPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        rows_per_page = self.kwargs.get('page_size')
        if rows_per_page:
            self.pagination_class.page_size = rows_per_page
        return queryset
    
class EmployeeList(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    #permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

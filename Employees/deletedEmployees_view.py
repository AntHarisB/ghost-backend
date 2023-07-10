from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from .employee_serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .employee_serializer import EmployeeSerializer
from django.contrib.auth.models import User
from rest_framework import generics

class PastEmployeePagination(PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })

class PastEmployeesList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        past_employees = User.objects.filter(profile__obrisan=True)
        serializer = EmployeeSerializer(past_employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PastEmployeesListPages(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    #permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    pagination_class = PastEmployeePagination

    def get_queryset(self):
        queryset =  User.objects.filter(profile__obrisan=True)
        rows_per_page = self.kwargs.get('page_size')
        if rows_per_page:
            self.pagination_class.page_size = rows_per_page
        return queryset
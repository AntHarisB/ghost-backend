from rest_framework import generics
from Invoicing.models import Invoicing
from .invoicing_serializer import InvoicingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ProjectInfoPagination(PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })

class PaidInvoicingView(generics.ListAPIView):
    serializer_class = InvoicingSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Invoicing.objects.all()
    pagination_class = ProjectInfoPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        rows_per_page = self.kwargs.get('page_size')
        if rows_per_page:
            self.pagination_class.page_size = rows_per_page

        queryset = queryset.filter(status='paid')
        return queryset
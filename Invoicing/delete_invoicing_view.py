from .models import Invoicing
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes


@permission_classes((permissions.AllowAny,))
class InvoicingDeleteView(APIView):
    queryset = Invoicing.objects.all()

    def delete(self, request, pk, format=None):
        try:
            invoicing = Invoicing.objects.get(pk=pk)
        except Invoicing.DoesNotExist:
            raise Http404
        
        invoicing.delete()

        return Response({'success': 'Invoicing deleted!'}, status=status.HTTP_204_NO_CONTENT)
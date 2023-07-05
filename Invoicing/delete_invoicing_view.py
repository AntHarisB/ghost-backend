from .models import Invoicing
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes


@permission_classes((permissions.AllowAny,))
class InvoicingDeleteView(APIView):
    lookup_field = 'id'
    
    def delete(self, request, id, format=None):
        try:
            invoicing = Invoicing.objects.get(id=id)
        except Invoicing.DoesNotExist:
            raise Http404
        
        invoicing.delete()

        return Response({'success': 'Invoicing deleted!'}, status=status.HTTP_204_NO_CONTENT)
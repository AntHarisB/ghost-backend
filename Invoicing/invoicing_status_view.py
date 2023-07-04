from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Invoicing
from .invoicing_serializer import InvoicingSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import permission_classes


@permission_classes((permissions.AllowAny,))
class StatusInvoicingView(generics.RetrieveUpdateAPIView):
    serializer_class = InvoicingSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Invoicing.objects.filter(pk=pk)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        paid_clicked = request.data.get('paid_clicked')
        sent_clicked = request.data.get('sent_clicked')

        if paid_clicked == 'paid':
            instance.paid = 'paid'

        if sent_clicked == 'sent':
            instance.sent = 'sent'

        if instance.paid == 'paid' and instance.sent == 'sent':
            instance.status = 'paid'
        elif instance.paid == 'unpaid' and instance.sent == 'sent':
            instance.status = 'sent'
        elif instance.paid == 'paid' and instance.sent == 'not sent':
            instance.status = 'not sent'
        else:
            instance.paid == 'unpaid' and instance.sent == 'not sent'
            instance.status = 'not sent'

        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)





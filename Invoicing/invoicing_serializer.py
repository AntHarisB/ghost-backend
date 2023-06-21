from rest_framework import serializers
from Invoicing.models import Invoicing

class InvoicingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoicing
        fields = ['id', 'client', 'industry', 'total_hours_billed', 'amount_billed', 'status', 'paid', 'sent']
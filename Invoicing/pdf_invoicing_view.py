from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Invoicing
import datetime

def generate_invoice_pdf(request, invoice_id):

    invoice = Invoicing.objects.get(id=invoice_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.id}.pdf"'
    p = canvas.Canvas(response)

    p.setFont('Helvetica-Bold', 14)
    p.drawString(100, 750, 'Ant Colony')

    p.setFont('Helvetica', 12)
    p.drawString(400, 750, str(datetime.date.today()))

    p.setFont('Helvetica', 12)
    p.drawString(100, 700, f'Client: {invoice.client}')
    p.drawString(100, 680, f'Total Hours Billed: {invoice.total_hours_billed}')
    p.drawString(100, 660, f'Amount Billed: {invoice.amount_billed}')

    p.save()
    return response


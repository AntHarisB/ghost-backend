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
    p.drawString(440, 750, str(datetime.date.today()))

    p.line(100, 745, 500, 745)

    p.setFont('Helvetica', 12)
    p.drawString(100, 690, f'Client: {invoice.client}')
    p.drawString(100, 670, f'Total Hours Billed: {invoice.total_hours_billed}')
    p.drawString(100, 650, f'Amount Billed: {invoice.amount_billed}')

    p.setFont('Helvetica', 10)
    p.drawString(100, 100, 'Ant Colony Team')
    p.drawString(375, 100, 'IT Services and IT Consulting')

    p.save()
    return response



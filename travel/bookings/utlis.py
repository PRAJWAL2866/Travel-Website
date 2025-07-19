import os
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.conf import settings


def generate_invoice(booking):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 750, "Travel Booking Invoice")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 700, f"Booking ID: {booking.id}")
    pdf.drawString(50, 680, f"Name: {booking.name}")
    pdf.drawString(50, 660, f"Email: {booking.email}")
    pdf.drawString(50, 640, f"Phone: {booking.phone}")
    pdf.drawString(50, 620, f"Destination: {booking.destination}")
    pdf.drawString(50, 600, f"Arrival Date: {booking.arrival_date}")
    pdf.drawString(50, 580, f"Leaving Date: {booking.leaving_date}")
    pdf.drawString(50, 560, f"Number of People: {booking.number_of_people}")
    #pdf.drawString(50, 540, f"Total Amount: ₹{booking.amount}")

    pdf.showPage()
    pdf.save()

    buffer.seek(0)

    invoice_filename = f"invoice_{booking.id}.pdf"
    invoice_path = os.path.join(settings.MEDIA_ROOT, invoice_filename)

    with open(invoice_path, "wb") as f:
        f.write(buffer.getvalue())

    return invoice_path

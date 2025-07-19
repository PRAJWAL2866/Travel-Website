from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import EmailMessage, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import login, authenticate
from .forms import BookingForm, ContactForm, RegistrationForm
from .models import Booking
from .utlis import generate_invoice

def send_email_with_invoice(subject, template_name, recipient_email, context, invoice_path=None):
    try:
        email_html = render_to_string(template_name, context)
        email_plain = strip_tags(email_html)

        email = EmailMessage(
            subject,
            email_plain,
            "your_email@gmail.com",  # Use the email from settings.py
            [recipient_email]
        )
        email.content_subtype = "html"  # Send HTML email

        if invoice_path:
            email.attach_file(invoice_path)  # Attach the invoice

        email.send()

    except BadHeaderError:
        print("Invalid email header found.")
    except Exception as e:
        print(f"Email sending failed: {e}")

def book_now(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # Generate Google Pay UPI Link
            upi_id = "7767084207@ybl"
            amount = 7000
            payment_link = f"upi://pay?pa={upi_id}&pn=Prajwal&am={amount}&cu=INR&tn=Trip Booking Payment"

            # Generate Invoice PDF
            invoice_path = generate_invoice(booking)

            # Send Booking Confirmation Email with Invoice
            send_email_with_invoice(
                subject="Booking Confirmation - Travel Agency",
                template_name='booking_email.html',
                recipient_email=booking.email,
                context={
                    'name': booking.name,
                    'destination': booking.destination,
                    'arrival_date': booking.arrival_date,
                    'leaving_date': booking.leaving_date,
                    'amount': amount,
                    'payment_link': payment_link,
                },
                invoice_path=invoice_path  # Attach invoice
            )

            messages.success(request, "Booking successful! A confirmation email with a payment link and invoice has been sent.")
            return redirect('booking_success')
        else:
            messages.error(request, "Booking failed. Please try again.")

    else:
        form = BookingForm()

    return render(request, 'Main.html', {'form': form})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            send_email_with_invoice(
                subject="We Received Your Message - Travel Agency",
                template_name='contact_email.html',
                recipient_email=contact.email,
                context={'name': contact.name}
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact_success')

        else:
            messages.error(request, "Failed to send message. Please try again.")

    else:
        form = ContactForm()

    return render(request, 'Main.html', {'contact_form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            send_email_with_invoice(
                subject="Welcome to Travel Agency!",
                template_name='registration_email.html',
                recipient_email=user.email,
                context={'username': username}
            )

            messages.success(request, f"Account created for {username}! A confirmation email has been sent.")
            return redirect('home')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

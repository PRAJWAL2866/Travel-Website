from django import forms
from .models import Booking, Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['booking_date']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'  # ✅ Include all fields


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

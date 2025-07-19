from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Booking, Contact  # Import the models

# Register Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'arrival_date', 'leaving_date', 'booking_date')  # Columns to display
    list_filter = ('destination', 'arrival_date', 'booking_date')  # Filters in the sidebar
    search_fields = ('name', 'email', 'phone')  # Searchable fields
    ordering = ('-booking_date',)  # Order by latest bookings

# Register Contact model
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'subject')
    search_fields = ('name', 'email', 'subject')

from django.urls import path
from django.views.generic import TemplateView
from .views import book_now, contact

urlpatterns = [
    path('book/', book_now, name='book'),
    path('contact/', contact, name='contact'),
    path('booking-success/', TemplateView.as_view(template_name='booking_success.html'), name='booking_success'),
]

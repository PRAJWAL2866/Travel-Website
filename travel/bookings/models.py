from django.db import models
from django.utils import timezone

class Booking(models.Model):
    DESTINATIONS = [
        ('Mumbai', 'Mumbai'),
        ('Sydney', 'Sydney'),
        ('Hawaii', 'Hawaii'),
        ('Spiti Valley', 'Spiti Valley'),
        ('Chandratal', 'Chandratal'),
        ('Vietnam', 'Vietnam'),
        ('Mount Fuji', 'Mount Fuji'),
        ('Himalayas', 'Himalayas'),
        ('Goa', 'Goa'),
        ('Rome', 'Rome'),
    ]

    name = models.CharField(max_length=100, default="")
    address = models.TextField(default="")
    phone = models.CharField(max_length=15, default="")
    email = models.EmailField(default="")
    destination = models.CharField(max_length=255, choices=DESTINATIONS, default='Mumbai')
    number_of_people = models.IntegerField()
    arrival_date = models.DateField()
    leaving_date = models.DateField()
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.destination} ({self.arrival_date} - {self.leaving_date})"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"

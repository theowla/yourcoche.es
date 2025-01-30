from django.db import models

class Car(models.Model):
    # Fields for the Car model

    # Auto-incremented ID field is created automatically by Django
    make = models.CharField(max_length=100)  # Make of the car (e.g., Toyota, Ford)
    model = models.CharField(max_length=100)  # Model of the car (e.g., Corolla, Mustang)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the car
    pictures = models.ImageField(upload_to='car_pictures/', null=True, blank=True)  # Picture of the car
    description = models.TextField()  # Description of the car
    STATE_CHOICES = [  # Choices for the state of the car
        ('Available', 'Available'),
        ('Sold', 'Sold'),
        ('Reserved', 'Reserved'),
    ]
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='available')  # State of the car

    # String representation for the admin panel and shell
    def __str__(self):
        return f"{self.make} {self.model} - {self.state}"

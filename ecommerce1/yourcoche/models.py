from django.db import models

class Car(models.Model):
    TRANSMISSION_MANUAL = 'manual'
    TRANSMISSION_AUTOMATIC = 'automatic'

    TRANSMISSION_CHOICES = [
        (TRANSMISSION_MANUAL, 'Manual'),
        (TRANSMISSION_AUTOMATIC, 'Automatic'),
    ]

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Fixed missing decimal_places
    km = models.DecimalField(max_digits=7, decimal_places=2)  # Fixed missing decimal_places
    year = models.PositiveIntegerField()  # Changed from DecimalField to PositiveIntegerField (better for years)
    motor = models.CharField(max_length=100)
    transmission = models.CharField(
        max_length=10,
        choices=TRANSMISSION_CHOICES,
        default=TRANSMISSION_MANUAL
    )

    def __str__(self):
        return f"{self.make} {self.model} - {self.get_transmission_display()}"


class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="car_images/")  # Store images in /media/car_images/

    def __str__(self):
        return f"Image for {self.car.make} {self.car.model}"

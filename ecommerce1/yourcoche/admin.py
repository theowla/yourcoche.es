from django.contrib import admin
from .models import Car, CarImage

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1  # Allows users to add at least one image

class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]  # Adds image upload fields directly in the Car admin
    list_display = ('make', 'model', 'year', 'price', 'transmission')  # Shows useful car info
    list_filter = ('transmission', 'year', 'make')  # Adds filtering options, including transmission
    search_fields = ('make', 'model', 'year')  # Enables search by make, model, or year
    ordering = ('-year',)  # Orders cars by the newest first

admin.site.register(Car, CarAdmin)  # Register Car with improved admin settings
admin.site.register(CarImage)

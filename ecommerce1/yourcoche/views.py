from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Car
from django.db.models import Q  # Import Q for complex queries

# Create your views here.
def home(request):
    cars = Car.objects.all()
    # Pass the cars to the template
    return render(request, 'index.html', {'cars': cars})

def contacto(request):
    return render(request, "contacto.html")

def search_cars(request):
    query = request.GET.get('query', '').strip()  # Get the search query and remove extra spaces
    cars = None  # Initialize cars to None in case no query is provided

    if query:  # Check if the query is not empty
        cars = Car.objects.filter(
            Q(make__icontains=query) | Q(model__icontains=query)
        )
    car_makes = Car.objects.values('make').distinct()  # Get unique car makes
    car_models = Car.objects.values('model').distinct()  # Get unique car makes
    
    return render(request, 'post.html', {'cars': cars, 'query': query, 'car_makes': car_makes, 'car_models': car_models})

def post(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, "carPost.html", {'car': car})

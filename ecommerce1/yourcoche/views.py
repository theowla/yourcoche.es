from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db.models import Max
from django.db.models import Min
from .models import Car
from django.db.models import Q  # Import Q for queries

def home(request):
    cars = Car.objects.all()
    # Pass the cars to the template
    return render(request, 'index.html', {'cars': cars})

def contacto(request):
    return render(request, "contacto.html") #renders the contact page

def search_cars(request):
    
    reset = request.GET.get('reset') #detects when the user whants to clear the page
    
    if (reset == 1): #lets you clear the search bar
        return render(request, 'post.html')
    
    # Get Max and Min Value input
    max_price = request.GET.get('priceMax', '')
    min_price = request.GET.get('priceMin', '')
    
    # Check if min_price is not empty
    if min_price.strip():  # .strip() removes leading and trailing spaces
        min_price_int = int(min_price)
    else:
        min_price_int = 1  # Default value if min_price is empty
        print("min_price is empty, defaulting to 1")

    # Check if max_price is not empty
    if max_price.strip():  # .strip() removes leading and trailing spaces
        max_price_int = int(max_price)
    else:
        max_price_int = 1000000  # Default value if max_price is empty
        print("max_price is empty, defaulting to 1.000.000")

    print(max_price, min_price)
 
    query = request.GET.get('query', '').strip()  # Get the search query and remove extra spaces
    cars = None  # Initialize cars to None in case no query is provided

    if query:  # Check if the query is not empty
        cars = Car.objects.filter(
            Q(make__icontains=query, price__range=(min_price_int, max_price_int)) | Q(model__icontains=query, price__range=(min_price_int, max_price_int)) 
        )
    queryText = request.GET.get('queryText', '').strip()  # Get the search query and remove extra spaces

    if queryText:  # Check if the query is not empty
        cars = Car.objects.filter(
            Q(make__icontains=queryText, price__range=(min_price_int, max_price_int)) | Q(model__icontains=queryText, price__range=(min_price_int, max_price_int)) 
        )
        
    car_makes = Car.objects.values('make').distinct()  # Get unique car makes
    if cars != None:
        car_model = Car.objects.values('model').filter(make__in=cars).distinct()  # Get unique car makes
    else: 
        car_model = Car.objects.values('model').distinct()
    
    return render(request, 'post.html', {'cars': cars, 'query': query, 'queryText': queryText, 'car_makes': car_makes, 'car_model': car_model, 'reset': reset})

def post(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, "carPost.html", {'car': car}) #renders the page and gives you all the data of the car you looked up

def about(request):
    return render(request, "aboutUs.html") #renders the about us page

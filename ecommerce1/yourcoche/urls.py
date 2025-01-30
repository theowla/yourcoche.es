from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contacto/", views.contacto, name="contacto"),
    path('search/', views.search_cars, name="search"),
    path('post/<int:id>/', views.post, name="post"),
    path('aboutUs/', views.about, name="aboutUs"),        
]
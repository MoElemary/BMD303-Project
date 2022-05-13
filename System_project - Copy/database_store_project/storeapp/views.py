from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Patient,ProductDetails
# Create your views here.


def homepage(request):
    contex = {
        'I': Product.objects.all()

    }
    return render(request, 'storeapp/home.html', contex)


def about_us(user_response):
    return render(user_response, 'storeapp/about.html', {'title': 'about'})


def Patient(request):
    contex_page = {
        'K': Patient.objects.all()
    }
    return render(request, 'storeapp/Customers.html', contex_page )
    #return render(user_response, 'store/home.html', contex)


def details(request):
    contex_page = {
        'L': ProductDetails.objects.all()
    }
    return render(request, 'storeapp/Details.html', contex_page )
    #return render(user_response, 'store/home.html', contex)


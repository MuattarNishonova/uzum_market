from django.shortcuts import render
from .models import Product_model


def Product_views(request):
    products = Product_model.objects.all()
    return render (request,"products/products.html",context={'products': products})

# Create your views here.

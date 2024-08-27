import json

from django.shortcuts import render
from .models import Product_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def Product_views(request):
    products = Product_model.objects.all()
    return render (request,"products/products.html",context={'products': products})

# Create your views here.
def product_detail(request,id):
    product = Product_model.objects.get(id=id)
    context = {
        'product': product
    }
    return render (request,"products/product-detail.html",context=context)


@csrf_exempt
def add_to_card(request):
    if request.method == 'POST':
        print(request.POST)
    return JsonResponse(data={'status':'Okey'})


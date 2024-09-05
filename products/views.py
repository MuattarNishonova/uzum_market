import json

from django.shortcuts import render
from .models import Product_model,Cart,CartItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404



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


def add_to_card(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        product = get_object_or_404(Product_model, id= product_id)
        # print(request.user)
        # product = Product_model.objects.get(id = product_id,)
        cart , created = Cart.objects.get_or_create(user=request.user, is_active=True)

        cart_item , item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not item_created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1


        cart_item.save()
        return JsonResponse(data={'status':'okey'})
        

    return JsonResponse(data={'status':'error'})


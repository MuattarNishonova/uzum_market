import json


from .models import Product_model,Cart,CartItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404,redirect,render
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from users.models import CustomUser,UserTypeChoise







def Product_views(request):
    products = Product_model.objects.all()
    search_q = request. GET. get('q', "")

    if search_q:
        products = products.filter(
            Q(name__icontains=search_q) | Q(description__icontains=search_q)
        )
    
    return render (request,"products/products.html",context={'products': products})

# Create your views here.
def product_detail(request,slug):
    product = Product_model.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render (request,"products/product-detail.html",context=context)

@login_required
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


def user_cart(request):
    if request.method == "GET":
        user: CustomUser = request.user
        

        

        if isinstance(user, AnonymousUser):
            messages.info(request, "Oldin login qilgin {}")
            return redirect("users:login")
        
        if user.user_type == UserTypeChoise.REGULAR:
            pass

        cart = Cart.objects.get(user=user, is_active=True)
        context = {
            'cart': cart
        }

        return render(
            request, 
            template_name='products/user_cart.html', 
            context=context)
    


def delete_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cart_item_id = data.get('cart_item_id')
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()
        return JsonResponse(data={'status':'okey'})
        

    return JsonResponse(data={'status':'error'})



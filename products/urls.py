from django.urls import path 
from .views import Product_views

urlpatterns = [
    path('product/',Product_views, name="product_urls")
]
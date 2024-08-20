from django.urls import path 
from .views import Product_views,product_detail

urlpatterns = [
    path('product/',Product_views, name="product_urls"),
    path('product/<int:id>/',product_detail, name='product-detail')

]
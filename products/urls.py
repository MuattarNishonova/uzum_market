from django.urls import path 
from .views import Product_views,product_detail,add_to_card

urlpatterns = [
    path('product/',Product_views, name="product_urls"),
    path('product/<int:id>/',product_detail, name='product-detail'),
    path('add_to_card/',add_to_card, name='add_to_card')

]
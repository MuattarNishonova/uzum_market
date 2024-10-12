from django.urls import path 
from .views import Product_views,product_detail,add_to_card,user_cart,delete_cart,pochts_junat

urlpatterns = [
    path('',Product_views, name="product_urls"),
    path('product/<slug:slug>/',product_detail, name='product-detail'),
    path('add_to_card/',add_to_card, name='add_to_card'),
    path('user-cart/', user_cart,name='user-cart'),
    path('delete-cart/',delete_cart,name='delete-cart'),
    path('pochta_junat/',pochts_junat,name='email_sending')

]
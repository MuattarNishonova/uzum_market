from django.contrib.admin import ModelAdmin,register,StackedInline
from .models import Category,Product_image,Product_image
# Register your models here.


class Product_imageStackedInline(StackedInline):
    model = Product_image
    fields = ('image','product')



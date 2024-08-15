from django.contrib.admin import ModelAdmin,register,StackedInline
from .models import Category,Product_model,Product_image
# Register your models here.


class Product_imageStackedInline(StackedInline):
    model = Product_image
    fields = ('image','product')

@register(Product_model)
class Product_modelModelAdmin(ModelAdmin):
    # inlines = [Product_imageStackedInline, ]
    # inlines = (Product_imageStackedInline, )
    inlines = Product_imageStackedInline, 
    list_display = 'name', 'category','price','quantity'

@register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass

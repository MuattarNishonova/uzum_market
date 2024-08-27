from django.contrib.admin import ModelAdmin,register,StackedInline
from .models import Category,Product_model,Product_image,Color,CartItem,Cart,Order,OrderItem
# Register your models here.


class Product_imageStackedInline(StackedInline):
    model = Product_image
    fields = ('image','product')


class Product_colorStackedInline(StackedInline):
    model = Color
    fields = ('name','product')

@register(Product_model)
class Product_modelModelAdmin(ModelAdmin):
    # inlines = [Product_imageStackedInline, ]
    # inlines = (Product_imageStackedInline, )  
    inlines = Product_imageStackedInline, Product_colorStackedInline
    list_display = 'name', 'category','price','quantity'

@register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@register(CartItem)
class CartItemModelAdmin(ModelAdmin):
    pass

@register(Cart)
class CartModelAdmin(ModelAdmin):
    pass

@register(Order)
class OrderModelAdmin(ModelAdmin):
    pass

@register(OrderItem)
class OrderItemModelAdmin(ModelAdmin):
    pass


from django.db.models import Model,CharField,TextField,PositiveIntegerField,ImageField,ForeignKey,CASCADE,FloatField

# Create your models here.

class Category(Model):
    name = CharField(max_length=255)
    parent = ForeignKey("self",on_delete=CASCADE,null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    

class Product_model(Model):
    name = CharField(max_length=1000)
    price = FloatField()
    discount = PositiveIntegerField()
    colour = CharField(max_length=200, null=True, blank=True)
    short_description = TextField()
    description = TextField()
    quantity = PositiveIntegerField(default=1)
    category = ForeignKey(Category,on_delete=CASCADE,related_name='products')

    def __str__(self) -> str:
        return   f"{self.name}"
    
    @property
    def first_image(self):
        return self.images.all().first()
    
    
    

class Product_image(Model):
    image = ImageField(upload_to='products')
    product = ForeignKey(Product_model,on_delete=CASCADE,related_name = 'images')   


class Color(Model):
    name = CharField(max_length=25)
    product = ForeignKey('products.Product_model',CASCADE,related_name="colors")
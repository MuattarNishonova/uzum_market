from django.db.models import Model,CharField,TextField,PositiveIntegerField,ImageField,ForeignKey,CASCADE,FloatField,DateTimeField,BooleanField,DecimalField,SlugField
from django.template.defaultfilters import slugify

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
    slug = SlugField(unique=True,blank=True,null=True)




    def save(self, *args,**kwargs):
        self.slug = slugify(self.name)
        
        super().save()



    def __str__(self) -> str:
        return   f"{self.name}"
    
    @property
    def first_image(self):
        return self.images.all().first()
    


    @property
    def get_price(self):
        if self.discount:
            price= self.price - (self.price*self.discount)/100
            return price
        return self.price

class Product_image(Model):
    image = ImageField(upload_to='products')
    product = ForeignKey(Product_model,on_delete=CASCADE,related_name = 'images')   


class Color(Model):
    name = CharField(max_length=25)
    product = ForeignKey('products.Product_model',CASCADE,related_name="colors")




# Cart models started


from django.contrib.auth import get_user_model
# from users.models import CustomUser


User = get_user_model()

class Cart(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    is_active = BooleanField(default=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())


class CartItem(Model):
    cart = ForeignKey(Cart, related_name='items', on_delete=CASCADE)
    product = ForeignKey(Product_model, on_delete=CASCADE)
    quantity = PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def total_price(self):
        return self.quantity * self.product.price


class Order(Model):
    user = ForeignKey(User, related_name='orders', on_delete=CASCADE)
    is_paid = BooleanField(default=False)
    payment_method = CharField(max_length=255)
    shipping_address = CharField(max_length=255)
    total_price = DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    def calculate_total_price(self):
        self.total_price = sum(item.total_price() for item in self.items.all())
        self.save()


class OrderItem(Model):
    order = ForeignKey(Order, related_name='items', on_delete=CASCADE)
    product = ForeignKey(Product_model, on_delete=CASCADE)
    quantity = PositiveIntegerField(default=1)
    price = DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order {self.order.id}"

    def total_price(self):
        return self.quantity * self.price
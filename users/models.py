from django.db.models import CharField
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    phone_number = CharField(max_length=25, default='111', blank=True, null= True)















# class User(Model):
#     username = CharField(max_length=100)
#     email = CharField(max_length=250)
#     phone_number = IntegerField()
    

#     def __str__(self) -> str:
#         return f"{self.username}"

    
from django.db.models import CharField,TextChoices
from django.contrib.auth.models import AbstractUser


class UserTypeChoise(TextChoices):
        ADMIN = 'admin',"Admin"
        OPERATOR = 'operator','Operator'
        REGULAR = 'regular','Regular'
        MODERATOR = 'moderator','Moderator'

class CustomUser(AbstractUser):
   
    user_type = CharField(max_length=20,choices=UserTypeChoise.choices,default=UserTypeChoise.REGULAR)
    phone_number = CharField(max_length=25, default='111', blank=True, null= True)
# user = CustomUser.objects.filter(
#       user_type = UserTypeChoise.OPERATOR
# )



#bitinchi admin databasega saqlanadi ikkinchisi qidiryatganda korinadigon
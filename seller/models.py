# from django.db.models import Model,TextField,CharField,PositiveIntegerField,EmailField,ForeignKey,CASCADE

# class SellerAccount(Model):
#     name = CharField(max_length=250)
#     phone_numer = CharField(max_length=200)
#     email = EmailField(max_length=250)
#     password = PositiveIntegerField()
#     language = CharField(max_length=250)

#     def __str__(self) -> str:
#         return self.name
    
# class Personal_Info(Model):
#     last_name = CharField(max_length=250)
#     name = CharField(max_length=250)
#     middle_name = CharField(max_length=250)
#     date_of_birth = CharField(max_length=100)
#     seller_account = ForeignKey(SellerAccount,on_delete=CASCADE,related_name='personal_info')

#     def __str__(self) -> str:
#         return   f"{self.name}"
    


# class Relation_info(Model):
#     last_name = CharField(max_length=250)
#     name = CharField(max_length=250)
#     middle_name = CharField(max_length=250)
#     phone_numer = CharField(max_length=200)
#     seller_account = ForeignKey(SellerAccount,on_delete=CASCADE,related_name='personal_info')

#     def __str__(self) -> str:
#         return   f"{self.name}"
    
# class Registratio_form(Model):
#     # legal_entity = 
#     YTT_nomi = CharField(max_length=500)
#     STIR = CharField(max_length=250)
#     IFUT = CharField(max_length=250)
#     seller_account = ForeignKey(SellerAccount,on_delete=CASCADE,related_name='personal_info')


#     def __str__(self) -> str:
#         return   f"{self.name}"
    

# class BillingAccount(Model):
#     bankcode = CharField(max_length=150)
#     account_number = PositiveIntegerField()
#     account_name = CharField(max_length=200)
#     seller_account = ForeignKey(SellerAccount,on_delete=CASCADE,related_name='personal_info')

#     def __str__(self) -> str:
#         return   f"{self.name}"




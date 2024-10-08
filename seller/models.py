# from django.db.models import Model,TextField,CharField,PositiveIntegerField,EmailField,ForeignKey,CASCADE

# class SellerAccount(Model):
#     name = CharField(max_length=250)
#     phonenumer = CharField(max_length=200)
#     email = EmailField(max_length=250)
#     password = PositiveIntegerField()
#     language = CharField(max_length=250)

#     def __str__(self) -> str:
#         return self.name
    
# class Personal_Info(Model):
#     last_name = CharField(max_length=250)
#     name = CharField(max_length=250)
#     middlename = CharField(max_length=250)
#     dateofbirth = CharField(max_length=100)
#     selleraccount = ForeignKey(SellerAccount,on_delete=CASCADE,related_name='personal_info')

#     def __str__(self) -> str:
#         return   f"{self.name}"
    


# class Relation_info(Model):
#     lastname = CharField(max_length=250)
#     name = CharField(max_length=250)
#     middlename = CharField(max_length=250)
#     phonenumer = CharField(max_length=200)
#     selleraccount = ForeignKey(SellerAccount,on_delete=CASCADE,related_name='personal_info')

#     def __str__(self) -> str:
#         return   f"{self.name}"
    
# class Registratio_form(Model):
#     # legal_entity = 
#     YTT_nomi = CharField(max_length=500)
#     STIR = CharField(max_length=250)
#     IFUT = CharField(max_length=250)
#     selleraccount = ForeignKey(SellerAccount,on_delete=CASCADE,related_name='personal_info')


#     def __str__(self) -> str:
#         return   f"{self.name}"
    

# class BillingAccount(Model):
#     bankcode = CharField(max_length=150)
#     accountnumber = PositiveIntegerField()
#     accountname = CharField(max_length=200)
#     selleraccount = ForeignKey(SellerAccount,on_delete=CASCADE,related_name='personal_info')

#     def __str__(self) -> str:
#         return   f"{self.name}"




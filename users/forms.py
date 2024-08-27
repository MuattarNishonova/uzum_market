from django.forms import ModelForm
from .models import CustomUser

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username",'password','email','first_name','last_name','phone_number')

    def save (self,commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
from django.contrib.admin import ModelAdmin,register,StackedInline
from .models import CustomUser


@register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    pass

# Register your models here.

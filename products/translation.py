from modeltranslation.translator import translator, TranslationOptions, register
from .models import Product_model, Category

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = 'name',

@register(Product_model)
class ProductTranslationOptions(TranslationOptions):
    fields = 'name','short_description','description',





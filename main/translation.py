from modeltranslation.translator import translator,TranslationOptions
from .models import *

class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)

class SubCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)

class ProductTranslationOptions(TranslationOptions):
    fields = ("name",'description','options')


class BannerTranslationOptions(TranslationOptions):
    fields = ("name",'description')


translator.register(Category, CategoryTranslationOptions) 
translator.register(SubCategory, SubCategoryTranslationOptions) 
translator.register(Product, ProductTranslationOptions) 
translator.register(Banner, BannerTranslationOptions) 
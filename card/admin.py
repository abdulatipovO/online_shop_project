from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CardProduct)
class CardProductAdmin(admin.ModelAdmin):
    list_display = ['product','qty','total_price']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['calculated_summa','sale','total_summa']
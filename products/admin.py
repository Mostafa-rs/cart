from django.contrib import admin
from .models import *

# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_price', 'total_price')


admin.site.register(Products, ProductsAdmin)
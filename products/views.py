from django.shortcuts import render
from .models import *

# Create your views here.


def prod_list(request):
    products = Products.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/products_list.html', context)
from django.shortcuts import render


# Create your views here.
from . import models


def product_list(request):
    products = models.Product.objects.all()
    return render(request, 'product/products.html', {
        'products': products
    })

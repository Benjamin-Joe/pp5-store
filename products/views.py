"Products Views"
from django.shortcuts import render
from .models import Product


def store(request):
    "View to return the all products shopping area"
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/store.html', context)

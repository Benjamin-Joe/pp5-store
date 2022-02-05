"Products Views"
from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def store(request):
    "View to return the all products shopping area"
    products = Product.objects.all()
    p = Paginator(Product.objects.all(), 12)
    page = request.GET.get('page')
    all_products = p.get_page(page)
    context = {
        'products': products,
        'all_products': all_products
    }
    return render(request, 'products/store.html', context)

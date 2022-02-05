"Products Views"
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product

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

# Code below came from Code Institute
def product_detail(request, product_id):
    "View to return a requested products details"
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
# End on taken code
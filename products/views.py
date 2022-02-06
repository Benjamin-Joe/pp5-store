"Products Views"
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product

def store(request):
    "View to return the all products shopping area"
    query = None
    products = Product.objects.all()
    p = Paginator(Product.objects.all(), 12)
    page = request.GET.get('page')
    all_products = p.get_page(page)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            all_products = products.filter(queries)

    context = {
        'products': products,
        'all_products': all_products,
        'search_term': query,
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
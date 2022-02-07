"Bag Views"
from django.shortcuts import render


def bag(request):
    "View to return the customer's bag"
    return render(request, 'bag/bag.html')

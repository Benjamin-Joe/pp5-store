"Bag Views"
from django.shortcuts import render, redirect


def bag(request):
    "View to return the customer's bag"
    return render(request, 'bag/bag.html')

#Code from Code Institute
def add_to_bag(request, item_id):
    "Add items to bag"
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    user_bag = request.session.get('user_bag', {})

    if item_id in list(user_bag.keys()):

        user_bag[item_id] += quantity
    else:
        user_bag[item_id] = quantity
    request.session['user_bag'] = user_bag
    print(request.session['user_bag'])
    return redirect(redirect_url)
# End of taken code
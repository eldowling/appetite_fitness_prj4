from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    subscription = None
    if 'purchase_subscription_id' in request.POST:
        subscription = request.POST.get('purchase_subscription_id')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    #if subscription:
    #    if item_id in list(basket.keys()):
    #        if subscription in basket[item_id]['items_subscription'].keys():
    #            basket[item_id]['items_subscription'][subscription] += quantity                
    #        else:
    #            basket[item_id]['items_subscription'][subscription] = quantity                
    #    else:
    #        basket[item_id] = {'items_subscription': {subscription: quantity}}
    #else:

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)

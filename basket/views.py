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
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    print("starting add_to_basket")
    if 'purchase_subscription_id' in request.POST:
        print("purchase_subscription_id is in the request.Post")
        subscription = request.POST.get('purchase_subscription_id')    
    basket = request.session.get('basket', {})
    print("subscription, quantity, redirect_url")
    print(subscription)
    print(quantity)
    print(redirect_url)

    if subscription:
        print("subscription is true, item_id")
        print(item_id)
        if item_id in list(basket.keys()):
            if subscription in basket[item_id]['items_subscription'].keys():
                basket[item_id]['items_subscription'][subscription] += quantity
            else:
                basket[item_id]['items_subscription'][subscription] = quantity
        else:
            basket[item_id] = {'items_subscription': {subscription: quantity}}
    else:

        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product, Sizes, Subscription_Type, Product_Subscription


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    subscription_size = None
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    print("starting add_to_basket")
    #if 'selected_subs_size_id' in request.POST:
    #    print("purchase_subscription_id is in the request.Post")
    subscription_size = request.POST.get('selected_subs_size_id')
    subs_size = str(subscription_size)
    #size = None
    #if 'purchase_size_id' in request.POST:
    #    size = request.POST.get('purchase_size_id')
    basket = request.session.get('basket', {})
    print("subscription_size", subs_size, "quantity", quantity)
    if subs_size != 'None' and product.has_sizes:
        if item_id in list(basket.keys()):
            if subs_size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][subs_size] += quantity
            else:
                basket[item_id]['items_by_size'][subs_size] = quantity
        else:
            basket[item_id] = {'items_by_size': {subs_size: quantity}}
    elif subs_size != 'None' and not product.has_sizes:
        if item_id in list(basket.keys()):
            if subs_size in basket[item_id]['item_subscription'].keys():
                basket[item_id]['item_subscription'][subs_size] += quantity
            else:
                basket[item_id]['item_subscription'][subs_size] = quantity
        else:
            basket[item_id] = {'item_subscription': {subs_size: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
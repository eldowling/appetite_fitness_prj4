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
    subscription_size = request.POST.get('selected_subs_size_id')
    subs_size = str(subscription_size)

    basket = request.session.get('basket', {})
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
    return redirect(redirect_url)

def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    subscription = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    if 'product_subs'in request.POST:
        subscription = request.POST['product_subs']
    basket = request.session.get('basket', {})

    if subscription:
        if quantity > 0:
            basket[item_id]['item_subscription'][subscription] = quantity
        else:
            del basket[item_id]['item_subscription'][subscription]
            if not basket[item_id]['item_subscription']:
                basket.pop(item_id)
    elif size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
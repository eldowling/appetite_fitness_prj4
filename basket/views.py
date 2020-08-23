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
    print('-----form items')
    print('qty, redir_url, selected_sub_id', quantity, redirect_url, subs_size)

    if request.POST:
        basket = request.session.get('basket', {})
        if subs_size != 'None' and product.has_sizes:       # Clothing item with only sizes
            if item_id in list(basket.keys()):
                if subs_size in basket[item_id]['items_by_size'].keys():
                    basket[item_id]['items_by_size'][subs_size] += quantity
                    messages.success(request,
                                    (f'Updated size {subs_size.upper()} '
                                    f'{product.name} quantity to '
                                    f'{basket[item_id]["items_by_size"][subs_size]}'))
                else:
                    basket[item_id]['items_by_size'][subs_size] = quantity
                    messages.success(request,
                                    (f'Added size {subs_size.upper()} '
                                    f'{product.name} to your basket'))
            else:
                basket[item_id] = {'items_by_size': {subs_size: quantity}}
                messages.success(request,
                                (f'Added size {subs_size.upper()} '
                                f'{product.name} to your basket'))
        else:                                             # Other items with subscriptions incl. Accessories
            if item_id in list(basket.keys()):
                if subs_size in basket[item_id]['item_subscription'].keys():
                    basket[item_id]['item_subscription'][subs_size] += quantity
                    if subs_size != 'None':
                        messages.success(request,
                                        (f'Updated subscription {subs_size} '
                                        f'{product.name} quantity to '
                                        f'{basket[item_id]["item_subscription"][subs_size]}'))
                    else: # for items without a size or subscription (such as accessories)
                        messages.success(request,
                                        (f'Updated {product.name} quantity to '
                                        f'{basket[item_id]["item_subscription"][subs_size]}'))     #update this
                else:
                    basket[item_id]['item_subscription'][subs_size] = quantity
                    if subs_size != 'None':
                        messages.success(request,
                                        (f'Added subscription {subs_size} '
                                        f'{product.name} to your basket'))
                    else: # for items without a size or subscription (such as accessories)
                        messages.success(request,
                                        (f'Added subscription {subs_size} '     #update this
                                        f'{product.name} to your basket'))
            else:
                basket[item_id] = {'item_subscription': {subs_size: quantity}}
                if subs_size != 'None':
                    messages.success(request,
                                    (f'Added subscription {subs_size} '
                                    f'{product.name} to your basket'))
                else:
                    # for items without a size or subscription (such as accessories)
                    messages.success(request,
                                    (f'Added subscription {subs_size} '     #update this
                                    f'{product.name} to your basket'))

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
            messages.success(request,
                             (f'Updated subscription {subscription} '
                              f'{product.name} quantity to '
                              f'{basket[item_id]["item_subscription"][subscription]}'))
        else:
            del basket[item_id]['item_subscription'][subscription]
            if not basket[item_id]['item_subscription']:
                basket.pop(item_id)
            messages.success(request,
                            (f'Removed subscription {subscription} '
                            f'{product.name} from your basket'))
    elif size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             (f'Updated size {size.upper()} '
                              f'{product.name} quantity to '
                              f'{basket[item_id]["items_by_size"][size]}'))
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request,
                        (f'Removed size {size.upper()} '
                        f'{product.name} from your basket'))

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))

def remove_from_basket(request, item_id):
    """Remove the item from the basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        subscription = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        if 'product_subs'in request.POST:
            subscription = request.POST['product_subs']
        basket = request.session.get('basket', {})
        print('----Size, Subs:', size, subscription)

        if subscription:
            del basket[item_id]['item_subscription'][subscription]
            if not basket[item_id]['item_subscription']:
                basket.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} - Subscription:  '
                              f'{subscription} from your basket'))
        elif size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} size '
                              f'{size.upper()} from your basket'))

        print('basket', basket)
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
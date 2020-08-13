from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Product_Subscription


def basket_contents(request):

    basket_items = []
    total = 0
    #non_delivery_total used to calculate deliver only on items that will be shipped (not online content / live classes)
    non_delivery_total = 0
    #sub_total is used to calculate total before any delivery (total + non_delivery_total)
    sub_total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        product_subscription = Product_Subscription.objects.filter(product=item_id)
        product = get_object_or_404(Product, pk=item_id)
        #if isinstance(item_data, int):            
        #    prod_sub = product_subscription.filter(product=product)
        #    for p in prod_sub:
        #        sub_price = p.price
        #    total += item_data * sub_price
        #    product_count += item_data
        #    basket_items.append({
        #        'item_id': item_id,
        #        'quantity': item_data,
        #        'product': product,
        #        'prod_sub': prod_sub,
        #    })
        #else:
        if 'items_by_size' in basket[item_id]:
            for subs_size, quantity in item_data['items_by_size'].items():
                prod_sub = product_subscription.filter(size=subs_size)
                for p in prod_sub:
                    sub_price = p.price
                    has_delivery = p.delivery_charge
                if has_delivery:                    
                    total += quantity * sub_price                    
                else:
                    non_delivery_total += quantity * sub_price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'subs_size': subs_size,
                    'prod_sub': prod_sub,
                })
        elif 'item_subscription' in basket[item_id]:
            for subs_size, quantity in item_data['item_subscription'].items():
                prod_sub = product_subscription.filter(subscription_type=subs_size)
                for p in prod_sub:
                    sub_price = p.price
                    has_delivery = p.delivery_charge
                if has_delivery:
                    total += quantity * sub_price
                else:
                    non_delivery_total += quantity * sub_price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'subs_size': subs_size,
                    'prod_sub': prod_sub,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    sub_total = total + non_delivery_total
    grand_total = delivery + total + non_delivery_total

    context = {
        'basket_items': basket_items,
        'total': total,
        'non_delivery_total': non_delivery_total,
        'sub_total': sub_total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

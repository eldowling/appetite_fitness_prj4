from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product, Product_Subscription, Sizes
from basket.contexts import basket_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    client_secret = 'temp client secret'

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in basket.items():
                try:
                    product = get_object_or_404(Product, pk=item_id)
                    product_subscription = Product_Subscription.objects.filter(product=item_id)
                    #if isinstance(item_data, int):
                    #    prod_sub = product_subscription.filter(product=product)
                    #    for p in prod_sub:
                    #        sub_price = p.price                            
                    #    order_line_item = OrderLineItem(
                    #        order=order,
                    #        product=product,
                    #        quantity=item_data,
                    #    )
                    #    order_line_item.save()
                    #else:
                    #    if 'items_by_size' in basket[item_id]:
                    #        for subs_size, quantity in item_data['items_by_size'].items():
                    #            prod_sub = product_subscription.filter(size=subs_size)
                    #            for p in prod_sub:
                    #                sub_price = p.price
                    #            order_line_item = OrderLineItem(
                    #                order=order,
                    #                product=product,
                    #                quantity=quantity,
                    #                product_subscription=subs_size,
                    #                product_size=prod_sub,
                    #            )
                    #            order_line_item.save()
                    if 'item_subscription' in basket[item_id]:
                        for subs_size, quantity in item_data['item_subscription'].items():
                            prod_sub = product_subscription.filter(subscription_type=subs_size)
                            selected_product_subs = get_object_or_404(Product_Subscription, pk=prod_sub[0].id)
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_subscription=selected_product_subs,
                            )

                            order_line_item.save()
                    elif 'items_by_size' in basket[item_id]:
                        for subs_size, quantity in item_data['items_by_size'].items():
                            prod_sub = product_subscription.filter(size=subs_size)
                            for p in prod_sub:
                                prod_size = p.size
                            sel_prod_size = get_object_or_404(Sizes, code=prod_size)
                            selected_product_subs = get_object_or_404(Product_Subscription, pk=prod_sub[0].id)
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_subscription=selected_product_subs,
                                product_size=sel_prod_size,
                            )

                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "A product in your basket was not found in our database."
                        "Please contact us for assistance")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

                request.session['save_info'] = 'save-info' in request.POST
                return redirect(reverse('checkout_success', args=[order.order_number]))
            else:
                messages.error(request, 'There is an error on the form. \
                    Please review the details entered')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "There are no items in your basket right now")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key has not been set.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order number: {order_number} has been processed successfully \
        A confirmation email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
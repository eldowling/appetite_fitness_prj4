from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Subcategory, Sizes, Subscription_Type, Product_Subscription

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    subcategories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'subcategory':
                sortkey = 'subcategory__code'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'subcategory' in request.GET:
            subcategories = request.GET['subcategory'].split(',')
            products = products.filter(subcategory__code__in=subcategories)
            subcategories = Subcategory.objects.filter(code__in=subcategories)

        if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request,
                                ("No search criteria was entered"))
                    return redirect(reverse('products'))

                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'current_subcategories': subcategories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show a single product details """
    product = get_object_or_404(Product, pk=product_id)
    product_subscription = product.product_subscription_set.all()
    # Default to the first subscription and display the price for this subscription
    #selected_subscription = Subscription_Type.objects.filter(id=product_id).first()
    #sel_product_subscription = product_subscription.filter(subscription_type=selected_subscription)
    selected_subs_size = None
    sel_product_subscription = None
    #sel_sub_price = None

    if request.POST:
        selected_subs_size = request.POST.get("selected_subs_size_id")
        if product.subscription:
            sel_product_subscription = product_subscription.filter(subscription_type=selected_subs_size)
        elif product.has_sizes:
            sel_product_subscription = product_subscription.filter(size=selected_subs_size)
        #sel_sub_price = request.POST.get("selected_subscription_price")
        
    context = {
        'product': product,
        'product_subscription': product_subscription,
        'selected_subs_size': selected_subs_size,
        'sel_product_subscription': sel_product_subscription,
        #'sel_sub_price': sel_sub_price,
    }

    return render(request, 'products/product_detail.html', context)
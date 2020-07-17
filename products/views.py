from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Subcategory, Sizes, Subscription_Type, Product_Subscription

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
    """ A view to show a single products details """

    product = get_object_or_404(Product, pk=product_id)
    product_subscription = product.product_subscription_set.all()
    #product_subscription = Product_Subscription.objects.filter(id=product_id).prefetch_related('product')
    #product_subscription =  Product_Subscription.objects.select_related('product').filter(id=product_id)
    #for prod_sub in product_subscription:
    #    print(prod_sub.product.name, prod_sub.subscription_type.name, prod_sub.price)
    sub_types = Subscription_Type.objects.filter(id=product_id)
    #for sub_type in sub_types:
    #   print(sub_type.name, sub_type.id)
    selected_subscription = None
   # sel_product_subscription = None
    #product_subscription = Product_Subscription.objects.all()

    if request.method == "POST":
        # Filter product_subscription by selected subscription, on a POST
        selected_subscription = request.POST.get("subscription")
        product_subscription = product_subscription.filter(subscription_type=selected_subscription)

    context = {
        'product': product,
        'product_subscription': product_subscription,
        'sub_types': sub_types,
        'selected_subscription': selected_subscription,
        #'sel_product_subscription': sel_product_subscription,
    }

    return render(request, 'products/product_detail.html', context)
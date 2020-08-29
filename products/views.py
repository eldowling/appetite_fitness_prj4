from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Product, Subcategory, Sizes, Subscription_Type, Product_Subscription, Subscriptions
from .forms import ProductForm

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    product_subscription = Product_Subscription.objects.all()
    subscriptions = Subscriptions.objects.all()
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
        'product_subscription': product_subscription,
        'subscriptions': subscriptions,
        'search_term': query,
        'current_subcategories': subcategories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show a details for a single product"""
    product = get_object_or_404(Product, pk=product_id)
    product_subscription = Product_Subscription.objects.filter(product=product)
    prod_sub_count = product_subscription.count()
    selected_subs_size = None
    sel_product_subscription = None

    # If product has no size and only 1 subscription - such as accessories, 
    # then set the values to populate the hidden field for adding to the basket
    if prod_sub_count == 1 and not product.has_sizes:
        for p in product_subscription:
            selected_subs_size = p.subscription_type.id
            sel_product_subscription = product_subscription

    if request.POST:
        selected_subs_size = request.POST.get("selected_subs_size_id")
        sel_sub_qty_available = request.POST.get("purch_qty_avail")
        if product.subscription and selected_subs_size != 'None':
            sel_product_subscription = product_subscription.filter(subscription_type=selected_subs_size)
        elif product.has_sizes:
            sel_product_subscription = product_subscription.filter(size=selected_subs_size)

    context = {
        'product': product,
        'product_subscription': product_subscription,
        'selected_subs_size': selected_subs_size,
        'sel_product_subscription': sel_product_subscription,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'The product has been added successfully')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

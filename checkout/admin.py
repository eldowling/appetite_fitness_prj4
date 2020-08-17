from django.contrib import admin
from .models import Order, OrderLineItem, Country


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total', 'lineitem_nondel_total',
                       'lineitem_deliverycost',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'non_delivery_total', 'grand_total', 
                       'original_basket', 'stripe_pid',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'non_delivery_total', 'grand_total', 
              'original_basket','stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'non_delivery_total',
                    'delivery_cost', 'grand_total',)

    ordering = ('-date',)

class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
    )
    ordering = ('code',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Country, CountryAdmin)



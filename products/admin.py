from django.contrib import admin
from .models import Product, Category, Subcategory, Subscription_Type, Sizes, Product_Subscription

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'description',
        'category',
        'subcategory',
        'subscription',
        'price',
        'quantity_available',
        'rating',
        'size',
        'colour',
        'image',
    )

    ordering = ('category', 'subcategory', 'name',)

class Product_SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'product',
        'subscription_type',
        'price',
        'quantity_available',
    )

    ordering = ('product', 'subscription_type',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
    )

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
    )

class Subscription_TypeAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
    )

class SizesAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
    )


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Subscription_Type, Subscription_TypeAdmin)
admin.site.register(Sizes, SizesAdmin)
admin.site.register(Product_Subscription, Product_SubscriptionAdmin)
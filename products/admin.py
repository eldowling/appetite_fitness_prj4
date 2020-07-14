from django.contrib import admin
from .models import Product, Category, Subcategory, Subscription_Type, Sizes, Product_Subscription

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Subscription_Type)
admin.site.register(Sizes)
admin.site.register(Product_Subscription)
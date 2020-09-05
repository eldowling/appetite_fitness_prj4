from django.urls import path
from . import views
from .views import Product_Subs_List

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('product_mgt/', views.product_mgt, name='product_mgt'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product,
         name='delete_product'),
    path('addprodsub/', views.add_product_subs, name='add_product_subs'),
    path('prodsubs_list/', Product_Subs_List.as_view(), name='prod_subs_list'),
    path('editprodsub/<int:product_subs_id>/', views.edit_product_subs, name='edit_product_subs'),
]